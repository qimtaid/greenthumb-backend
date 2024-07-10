from flask_restful import Resource, reqparse
from models import Schedule, db

class ScheduleResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('fitness_class_id', type=int, required=True, help='Fitness class ID cannot be blank.')
    parser.add_argument('date', type=str, required=True, help='Date cannot be blank.')

    def get(self, schedule_id=None):
        if schedule_id:
            schedule = Schedule.query.get(schedule_id)
            if schedule:
                return schedule.to_dict()
            return {'message': 'Schedule not found'}, 404
        schedules = Schedule.query.all()
        return [schedule.to_dict() for schedule in schedules]

    def post(self):
        data = ScheduleResource.parser.parse_args()
        new_schedule = Schedule(fitness_class_id=data['fitness_class_id'], date=data['date'])
        db.session.add(new_schedule)
        db.session.commit()
        return new_schedule.to_dict(), 201

    def put(self, schedule_id):
        data = ScheduleResource.parser.parse_args()
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            schedule.fitness_class_id = data['fitness_class_id']
            schedule.date = data['date']
            db.session.commit()
            return schedule.to_dict()
        return {'message': 'Schedule not found'}, 404

    def delete(self, schedule_id):
        schedule = Schedule.query.get(schedule_id)
        if schedule:
            db.session.delete(schedule)
            db.session.commit()
            return {'message': 'Schedule deleted'}
        return {'message': 'Schedule not found'}, 404
