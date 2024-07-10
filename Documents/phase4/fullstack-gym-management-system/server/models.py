from app import db
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Add other models (Member, Trainer, FitnessClass, etc.) below

class Member(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    membership_type = db.Column(db.String(50), nullable=False)

class Trainer(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    specialty = db.Column(db.String(50), nullable=False)

class FitnessClass(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainer.id'), nullable=False)
    trainer = db.relationship('Trainer')

class Schedule(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    fitness_class_id = db.Column(db.Integer, db.ForeignKey('fitness_class.id'), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    fitness_class = db.relationship('FitnessClass')

class Attendance(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    fitness_class_id = db.Column(db.Integer, db.ForeignKey('fitness_class.id'), nullable=False)
    member = db.relationship('Member')
    fitness_class = db.relationship('FitnessClass')

class Payment(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    member = db.relationship('Member')
