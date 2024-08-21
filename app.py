from flask import Flask, request, send_from_directory, jsonify, make_response, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from models import db, User, Plant, CareSchedule, Tips, ForumPost, GardenLayout, Comment  # Ensure Comment model is imported

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///greenthumb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you-will-never-guess'  # Ideally, use an environment variable
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'  # Ideally, use an environment variable
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize extensions
CORS(app, supports_credentials=True)
CORS(app, resources={r"/api/*": {"origins": "*"}})
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Helper function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the GreenThumb app!"}), 200

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "Username already exists"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"msg": "Email already exists"}), 400

    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"msg": "User not found"}), 401

    if not user.check_password(password):
        return jsonify({"msg": "Invalid password"}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    response = make_response(jsonify(access_token=access_token, refresh_token=refresh_token), 200)
    #response.set_cookie('jwt', access_token, httponly=True)
    #response.set_cookie('refresh_jwt', refresh_token, httponly=True, path='/refresh')

    return response

@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    response = make_response(jsonify(access_token=new_access_token), 200)
    #response.set_cookie('jwt', new_access_token, httponly=True)
    return response

@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({"msg": "Logged out successfully"}), 200)
    #response.delete_cookie('jwt')
    #response.delete_cookie('refresh_jwt')
    return response

@app.route('/plants', methods=['POST'])
@jwt_required()
def add_plant():
    data = request.json  # Expecting JSON data

    name = data.get('name')
    description = data.get('description')
    img_url = data.get('img_url')
    user_id = get_jwt_identity()

    if not name:
        return jsonify({"error": "Plant name is required"}), 400

    if not img_url:
        return jsonify({"error": "Image URL is required"}), 400

    # Save the plant details to the database
    new_plant = Plant(name=name, description=description, img_url=img_url, user_id=user_id)
    db.session.add(new_plant)
    db.session.commit()

    return jsonify({"message": "Plant added successfully"}), 201

@app.route('/plants', methods=['GET'])
@jwt_required()
def get_plants():
    user_id = get_jwt_identity()
    plants = Plant.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": plant.id, "name": plant.name, "img_url": plant.img_url, "description": plant.description} for plant in plants]), 200

@app.route('/plants/<int:plant_id>', methods=['PATCH'])
@jwt_required()
def update_plant(plant_id):
    data = request.get_json()
    plant = Plant.query.get_or_404(plant_id)
    user_id = get_jwt_identity()

    if plant.user_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    if 'name' in data:
        plant.name = data['name']
    if 'img_url' in data:
        plant.img_url = data['img_url']
    if 'description' in data:
        plant.description = data['description']

    db.session.commit()

    return jsonify({"msg": "Plant updated successfully"}), 200

@app.route('/plants/<int:plant_id>', methods=['DELETE'])
@jwt_required()
def delete_plant(plant_id):
    plant = Plant.query.get_or_404(plant_id)
    user_id = get_jwt_identity()

    if plant.user_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(plant)
    db.session.commit()

    return jsonify({"msg": "Plant deleted successfully"}), 200

# Care Schedule Management
@app.route('/care_schedules', methods=['GET'])
@jwt_required()
def get_care_schedules():
    print("GET /care_schedules route hit")  # Debugging line
    try:
        user_id = get_jwt_identity()
        plant_id = request.args.get('plant_id')

        if plant_id:
            schedules = CareSchedule.query.filter_by(user_id=user_id, plant_id=plant_id).all()
        else:
            schedules = CareSchedule.query.filter_by(user_id=user_id).all()

        if not schedules:
            return jsonify({"message": "No care schedules found."}), 404
        
        return jsonify([schedule.to_dict() for schedule in schedules]), 200

    except Exception as e:
        print(f"Error retrieving care schedules: {e}")  # Debugging line
        return jsonify({"error": "An error occurred while retrieving care schedules"}), 500


@app.route('/care_schedules', methods=['POST'])
@jwt_required()
def add_care_schedule():
    try:
        data = request.json
        if not data:
            raise ValueError("No data provided")

        plant_id = data.get('plant_id')
        task = data.get('task')
        schedule_date_str = data.get('schedule_date')
        interval = data.get('interval')

        if not plant_id or not task or not schedule_date_str or not interval:
            raise ValueError("Missing required fields")

        # Use dateutil to parse various date formats
        # schedule_date = parser.isoparse(schedule_date_str)

        care_schedule = CareSchedule(
            plant_id=plant_id,
            task=CareType[task],
            schedule_date=schedule_date,
            interval=ScheduleInterval[interval]
        )

        db.session.add(care_schedule)
        db.session.commit()

        return jsonify(care_schedule.to_dict()), 201

    except ValueError as e:
        print(f"ValueError: {e}")  # Debugging line
        return jsonify({"error": str(e)}), 400
    except KeyError as e:
        print(f"KeyError: {e}")  # Debugging line
        return jsonify({"error": f"Invalid key: {e}"}), 400
    except Exception as e:
        print(f"Error adding care schedule: {e}")  # Debugging line
        return jsonify({"error": "An error occurred while adding the care schedule"}), 500

@app.route('/care_schedules/<int:id>', methods=['PATCH'])
@jwt_required()
def update_care_schedule(id):
    try:
        schedule = CareSchedule.query.get_or_404(id)
        user_id = get_jwt_identity()

        if schedule.user_id != user_id:
            return jsonify({"error": "Unauthorized access"}), 403

        task = request.json.get('task')
        schedule_date = request.json.get('schedule_date')
        interval = request.json.get('interval')

        if task:
            schedule.task = task
        if schedule_date:
            try:
                schedule.schedule_date = datetime.strptime(schedule_date, '%Y-%m-%d')
            except ValueError:
                return jsonify({"error": "Invalid date format. Expected YYYY-MM-DD"}), 400
        if interval:
            schedule.interval = interval
        
        db.session.commit()
        return jsonify({"msg": "Care schedule updated successfully", "schedule": schedule.to_dict()}), 200

    except Exception as e:
        print(f"Error updating care schedule: {e}")  # Debugging line
        return jsonify({"error": "An error occurred while updating the care schedule"}), 500

@app.route('/care_schedules/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_care_schedule(id):
    try:
        schedule = CareSchedule.query.get_or_404(id)
        user_id = get_jwt_identity()

        if schedule.user_id != user_id:
            return jsonify({"error": "Unauthorized access"}), 403

        db.session.delete(schedule)
        db.session.commit()
        return jsonify({"msg": "Care schedule deleted successfully"}), 200

    except Exception as e:
        print(f"Error deleting care schedule: {e}")  # Debugging line
        return jsonify({"error": "An error occurred while deleting the care schedule"}), 500



# Tips Management
@app.route('/tips', methods=['POST'])
@jwt_required()
def add_tip():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author_id = get_jwt_identity()
    new_tip = Tips(title=title, content=content, author_id=author_id)
    db.session.add(new_tip)
    db.session.commit()
    return jsonify({"msg": "Tip added successfully"}), 201

@app.route('/tips', methods=['GET'])
def get_tips():
    tips = Tips.query.all()
    return jsonify([{"id": tip.id, "title": tip.title, "content": tip.content, "author_id": tip.author_id} for tip in tips]), 200

@app.route('/tips/<int:tip_id>', methods=['PATCH'])
@jwt_required()
def update_tip(tip_id):
    data = request.get_json()
    tip = Tips.query.get_or_404(tip_id)
    user_id = get_jwt_identity()

    if tip.author_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    if 'title' in data:
        tip.title = data['title']
    if 'content' in data:
        tip.content = data['content']

    db.session.commit()

    return jsonify({"msg": "Tip updated successfully"}), 200

@app.route('/tips/<int:tip_id>', methods=['DELETE'])
@jwt_required()
def delete_tip(tip_id):
    tip = Tips.query.get_or_404(tip_id)
    user_id = get_jwt_identity()

    if tip.author_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(tip)
    db.session.commit()

    return jsonify({"msg": "Tip deleted successfully"}), 200

# Forum Management
@app.route('/forum', methods=['POST'])
@jwt_required()
def add_forum_post():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    author_id = get_jwt_identity()

    new_post = ForumPost(title=title, content=content, author_id=author_id)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({"msg": "Forum post added successfully", "post": new_post.id}), 201

@app.route('/forum', methods=['GET'])
def get_forum_posts():
    posts = ForumPost.query.all()
    return jsonify([
        {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "author_id": post.author_id,
            "comments": [
                {"id": comment.id, "content": comment.content, "author_id": comment.author_id}
                for comment in post.comments
            ]
        } for post in posts
    ]), 200

@app.route('/forum/<int:post_id>', methods=['PATCH'])
@jwt_required()
def update_forum_post(post_id):
    data = request.get_json()
    post = ForumPost.query.get_or_404(post_id)
    user_id = get_jwt_identity()

    if post.author_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    if 'title' in data:
        post.title = data['title']
    if 'content' in data:
        post.content = data['content']

    db.session.commit()

    return jsonify({"msg": "Forum post updated successfully"}), 200

@app.route('/forum/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_forum_post(post_id):
    post = ForumPost.query.get_or_404(post_id)
    user_id = get_jwt_identity()

    # Debugging output
    print(f"User ID from token: {user_id}")
    print(f"Post author ID: {post.author_id}")

    if post.author_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(post)
    db.session.commit()

    return jsonify({"msg": "Forum post deleted successfully"}), 200




# Comment Management
@app.route('/forum/<int:post_id>/comments', methods=['GET'])
@jwt_required()
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([{
        "id": comment.id,
        "content": comment.content,
        "author_id": comment.author_id
    } for comment in comments]), 200



@app.route('/forum/<int:post_id>/comments', methods=['POST'])
@jwt_required()
def add_comment(post_id):
    data = request.get_json()
    content = data.get('content')
    author_id = get_jwt_identity()

    post = ForumPost.query.get_or_404(post_id)
    new_comment = Comment(content=content, author_id=author_id, post_id=post.id)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({"msg": "Comment added successfully", "comment": new_comment.id}), 201

@app.route('/forum/<int:post_id>/comments/<int:comment_id>', methods=['PATCH'])
@jwt_required()
def update_comment(post_id, comment_id):
    data = request.get_json()
    comment = Comment.query.get_or_404(comment_id)
    user_id = get_jwt_identity()

    if comment.author_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    if 'content' in data:
        comment.content = data['content']

    db.session.commit()

    return jsonify({"msg": "Comment updated successfully"}), 200

@app.route('/forum/<int:post_id>/comments/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(post_id, comment_id):
    comment = Comment.query.get_or_404(comment_id)
    user_id = get_jwt_identity()

    if comment.author_id != user_id:
        return jsonify({"msg": "Unauthorized"}), 403

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"msg": "Comment deleted successfully"}), 200

# Garden Layout Management

@app.route('/layout', methods=['POST'])
@jwt_required()
def add_garden_layout():
    data = request.get_json()
    name = data.get('name')
    layout_data = data.get('layout_data')
    user_id = get_jwt_identity()

    if not name or not layout_data:
        return jsonify({"msg": "Missing required data"}), 400

    new_layout = GardenLayout(name=name, layout_data=layout_data, user_id=user_id)
    db.session.add(new_layout)
    db.session.commit()
    return jsonify({"msg": "Garden layout added successfully"}), 201


@app.route('/layout', methods=['GET'])
@jwt_required()
def get_garden_layouts():
    user_id = get_jwt_identity()
    layouts = GardenLayout.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": layout.id, "name": layout.name, "layout_data": layout.layout_data} for layout in layouts]), 200




# File uploads handling
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
