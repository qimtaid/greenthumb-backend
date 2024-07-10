from flask_restful import Resource, reqparse
from models import FitnessClass, db

class FitnessClassResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name cannot be blank.')
    parser.add_argument('trainer_id', type=int, required=True, help='Trainer ID cannot be blank.')

    def get(self, fitness_class_id=None):
        if fitness_class_id:
            fitness_class = FitnessClass.query.get(fitness_class_id)
            if fitness_class:
                return fitness_class.to_dict()
            return {'message': 'Fitness class not found'}, 404
        fitness_classes = FitnessClass.query.all()
        return [fitness_class.to_dict() for fitness_class in fitness_classes]

    def post(self):
        data = FitnessClassResource.parser.parse_args()
        new_fitness_class = FitnessClass(name=data['name'], trainer_id=data['trainer_id'])
        db.session.add(new_fitness_class)
        db.session.commit()
        return new_fitness_class.to_dict(), 201

    def put(self, fitness_class_id):
        data = FitnessClassResource.parser.parse_args()
        fitness_class = FitnessClass.query.get(fitness_class_id)
        if fitness_class:
            fitness_class.name = data['name']
            fitness_class.trainer_id = data['trainer_id']
            db.session.commit()
            return fitness_class.to_dict()
        return {'message': 'Fitness class not found'}, 404

    def delete(self, fitness_class_id):
        fitness_class = FitnessClass.query.get(fitness_class_id)
        if fitness_class:
            db.session.delete(fitness_class)
            db.session.commit()
            return {'message': 'Fitness class deleted'}
        return {'message': 'Fitness class not found'}, 404
