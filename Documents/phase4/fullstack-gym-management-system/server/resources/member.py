from flask_restful import Resource, reqparse
from models import Member, db

class MemberResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank.')
    parser.add_argument('membership_type', type=str, required=True, help='Membership type cannot be blank.')

    def get(self, member_id=None):
        if member_id:
            member = Member.query.get(member_id)
            if member:
                return member.to_dict()
            return {'message': 'Member not found'}, 404
        members = Member.query.all()
        return [member.to_dict() for member in members]

    def post(self):
        data = MemberResource.parser.parse_args()
        new_member = Member(name=data['name'], membership_type=data['membership_type'])
        db.session.add(new_member)
        db.session.commit()
        return new_member.to_dict(), 201

    def put(self, member_id):
        data = MemberResource.parser.parse_args()
        member = Member.query.get(member_id)
        if member:
            member.name = data['name']
            member.membership_type = data['membership_type']
            db.session.commit()
            return member.to_dict()
        return {'message': 'Member not found'}, 404

    def delete(self, member_id):
        member = Member.query.get(member_id)
        if member:
            db.session.delete(member)
            db.session.commit()
            return {'message': 'Member deleted'}
        return {'message': 'Member not found'}, 404
