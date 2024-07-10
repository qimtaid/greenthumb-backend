from app import app, db
from models import User, Member, Trainer, FitnessClass, Schedule, Attendance, Payment
from faker import Faker

faker = Faker()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Creating a default admin user
    admin = User(username='admin', email='admin@example.com')
    admin.set_password('admin')
    db.session.add(admin)

    # Seeding other tables with Faker data
    for _ in range(10):
        member = Member(name=faker.name(), membership_type=faker.word())
        db.session.add(member)

        trainer = Trainer(name=faker.name(), specialty=faker.word())
        db.session.add(trainer)

        fitness_class = FitnessClass(name=faker.word(), trainer_id=trainer.id)
        db.session.add(fitness_class)

        schedule = Schedule(fitness_class_id=fitness_class.id, date=str(faker.date()))
        db.session.add(schedule)

        attendance = Attendance(member_id=member.id, fitness_class_id=fitness_class.id)
        db.session.add(attendance)

        payment = Payment(member_id=member.id, amount=faker.random_number(digits=2), date=str(faker.date()))
        db.session.add(payment)

    db.session.commit()
