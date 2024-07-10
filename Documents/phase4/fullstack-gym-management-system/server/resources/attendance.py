from flask_restful import Resource, reqparse
from models import Attendance, db

class AttendanceResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('member_id', type=int, required=True, help='Member ID cannot be blank.')
    parser.add_argument('fitness_class_id', type=int, required=True, help='Fitness class ID cannot be blank.')
    parser.add_argument('date', type=str, required=True, help='Date cannot be blank.')

    def get(self, attendance_id=None):
        if attendance_id:
            attendance = Attendance.query.get(attendance_id)
            if attendance:
                return attendance.to_dict()
            return {'message': 'Attendance not found'}, 404
        attendances = Attendance.query.all()
        return [attendance.to_dict() for attendance in attendances]

    def post(self):
        data = AttendanceResource.parser.parse_args()
        new_attendance = Attendance(member_id=data['member_id'], fitness_class_id=data['fitness_class_id'], date=data['date'])
        db.session.add(new_attendance)
        db.session.commit()
        return new_attendance.to_dict(), 201

    def put(self, attendance_id):
        data = AttendanceResource.parser.parse_args()
        attendance = Attendance.query.get(attendance_id)
        if attendance:
            attendance.member_id = data['member_id']
            attendance.fitness_class_id = data['fitness_class_id']
            attendance.date = data['date']
            db.session.commit()
            return attendance.to_dict()
        return {'message': 'Attendance not found'}, 404

    def delete(self, attendance_id):
        attendance = Attendance.query.get(attendance_id)
        if attendance:
            db.session.delete(attendance)
            db.session.commit()
            return {'message': 'Attendance deleted'}
        return {'message': 'Attendance not found'}, 404
