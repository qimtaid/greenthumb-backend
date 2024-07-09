from flask_restful import Resource, reqparse
from models import db, Event

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title is required')
parser.add_argument('description', type=str)
parser.add_argument('date', type=str, required=True, help='Date is required')

class EventListResource(Resource):
    def get(self):
        events = Event.query.all()
        return [{'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date} for event in events]

    def post(self):
        args = parser.parse_args()
        event = Event(title=args['title'], description=args['description'], date=args['date'])
        db.session.add(event)
        db.session.commit()
        return {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date}, 201

class EventResource(Resource):
    def get(self, event_id):
        event = Event.query.get_or_404(event_id)
        return {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date}

    def put(self, event_id):
        args = parser.parse_args()
        event = Event.query.get_or_404(event_id)
        event.title = args['title']
        event.description = args['description']
        event.date = args['date']
        db.session.commit()
        return {'id': event.id, 'title': event.title, 'description': event.description, 'date': event.date}

    def delete(self, event_id):
        event = Event.query.get_or_404(event_id)
        db.session.delete(event)
        db.session.commit()
        return '', 204
