from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from config import app, db
from resources.event import EventListResource, EventResource

# Initialize app and extensions
app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

# API routes
api.add_resource(EventListResource, '/events')
api.add_resource(EventResource, '/events/<int:event_id>')

if __name__ == '__main__':
    app.run(debug=True)
