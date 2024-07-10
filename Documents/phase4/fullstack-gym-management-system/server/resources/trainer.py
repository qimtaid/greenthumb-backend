from flask_restful import Resource, reqparse
from models import Trainer, db

class TrainerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank.')
    parser.add_argument('specialty', type=str, required=True, help='Specialty cannot be blank.')

    def get(self, trainer_id=None):
        if trainer_id:
            trainer = Trainer.query.get(trainer_id)
            if trainer:
                return trainer.to_dict()
            return {'message': 'Trainer not found'}, 404
        trainers = Trainer.query.all()
        return [trainer.to_dict() for trainer in trainers]

    def post(self):
        data = TrainerResource.parser.parse_args()
        new_trainer = Trainer(name=data['name'], specialty=data['specialty'])
        db.session.add(new_trainer)
        db.session.commit()
        return new_trainer.to_dict(), 201

    def put(self, trainer_id):
        data = TrainerResource.parser.parse_args()
        trainer = Trainer.query.get(trainer_id)
        if trainer:
            trainer.name = data['name']
            trainer.specialty = data['specialty']
            db.session.commit()
            return trainer.to_dict()
        return {'message': 'Trainer not found'}, 404

    def delete(self, trainer_id):
        trainer = Trainer.query.get(trainer_id)
        if trainer:
            db.session.delete(trainer)
            db.session.commit()
            return {'message': 'Trainer deleted'}
        return {'message': 'Trainer not found'}, 404
