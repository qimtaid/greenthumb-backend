from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)
jwt = JWTManager(app)

# Importing routes
from resources import member, trainer, fitness_class, schedule, attendance, payment, user

app.register_blueprint(user.bp)
app.register_blueprint(member.bp)
app.register_blueprint(trainer.bp)
app.register_blueprint(fitness_class.bp)
app.register_blueprint(schedule.bp)
app.register_blueprint(attendance.bp)
app.register_blueprint(payment.bp)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Gym Management System API"})

if __name__ == '__main__':
    app.run(debug=True)
