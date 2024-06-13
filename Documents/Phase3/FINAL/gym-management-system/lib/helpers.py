from models.member import Member
from models.trainer import Trainer
from models.attendance import Attendance
from models.fitness_class import FitnessClass
from models.payment import Payment
from datetime import datetime

def exit_program():
    print("Goodbye!")
    exit()

def list_members():
    members = Member.get_all_members()
    for member in members:
        print(member)

def find_member_by_name():
    name = input("Enter the member's name: ")
    members = Member.find_by_name(name)
    if members:
        for member in members:
            print(member)
    else:
        print(f'Member with name "{name}" not found')

def find_member_by_id():
    member_id = input("Enter the member's id: ")
    member = Member.find_by_id(member_id)
    if member:
        print(member)
    else:
        print(f'Member with id "{member_id}" not found')

def create_member():
    name = input("Enter the member's name: ")
    email = input("Enter the member's email: ")
    gender = input("Enter the member's gender: ")
    age = input("Enter the member's age: ")
    contact = input("Enter the member's contact: ")
    join_date = datetime.today().strftime('%Y-%m-%d')
    Member.add_member(name, email, gender, age, join_date, contact)
    print("Member created successfully!")

def update_member():
    member_id = input("Enter the member's id: ")
    member = Member.find_by_id(member_id)
    if member:
        name = input("Enter the new name for the member: ")
        email = input("Enter the new email for the member: ")
        gender = input("Enter the new gender for the member: ")
        age = input("Enter the new age for the member: ")
        contact = input("Enter the new contact for the member: ")
        member.update(name, email, gender, age, contact)
        print("Member updated successfully!")
    else:
        print(f'Member with id "{member_id}" not found')

def delete_member():
    member_id = input("Enter the member's id: ")
    member = Member.find_by_id(member_id)
    if member:
        member.delete_member(member_id)
        print("Member deleted successfully!")
    else:
        print(f'Member with id "{member_id}" not found')

def list_trainers():
    trainers = Trainer.get_all_trainers()
    for trainer in trainers:
        print(trainer )

def find_trainer_by_name():
    name = input("Enter the trainer's name: ")
    trainers = Trainer.find_by_name(name)
    if trainers:
        for trainer in trainers:
            print(trainer)
    else:
        print(f'Trainer with name "{name}" not found')

def find_trainer_by_id():
    trainer_id = input("Enter the trainer's id: ")
    trainer = Trainer.find_by_id(trainer_id)
    if trainer:
        print(trainer)
    else:
        print(f'Trainer with id "{trainer_id}" not found')

def create_trainer():
    name = input("Enter the trainer's name: ")
    email = input("Enter the trainer's email: ")
    age = input("Enter the trainer's age: ")
    gender = input("Enter the trainer's gender: ")
    specialization = input("Enter the trainer's specialty: ")
    hire_date = datetime.today().strftime('%Y-%m-%d')
    contact = input("Enter the trainer's contact: ")
    Trainer.add_trainer(name, email, age, specialization, gender, hire_date, contact)
    print("Trainer created successfully!")

def update_trainer():
    trainer_id = input("Enter the trainer's id: ")
    trainer = Trainer.find_by_id(trainer_id)
    if trainer:
        name = input("Enter the new name for the trainer: ")
        email = input("Enter the new email for the trainer: ")
        age = input("Enter the new age for the trainer: ")
        gender = input("Enter the new gender for the trainer: ")
        specialization = input("Enter the new specialty for the trainer: ")
        contact = input("Enter the new contact for the trainer: ")
        trainer.update(name, email, age, specialization, gender, contact)
        print("Trainer updated successfully!")
    else:
        print(f'Trainer with id "{trainer_id}" not found')

def delete_trainer():
    trainer_id = input("Enter the trainer's id: ")
    trainer = Trainer.find_by_id(trainer_id)
    if trainer:
        trainer.delete()
        print("Trainer deleted successfully!")
    else:
        print(f'Trainer with id "{trainer_id}" not found')

def list_attendance_records():
    attendances = Attendance.get_all_attendance()
    for attendance in attendances:
        print(attendance)

def add_attendance_record():
    member_id = input("Enter the member's ID: ")
    class_id = input("Enter the class ID: ")
    date = input("Enter the date (YYYY-MM-DD): ")
    Attendance.add_attendance_record(member_id, class_id, date)
    print("Attendance record added successfully!")

def list_fitness_classes():
    classes = FitnessClass.get_all_fitness_classes()
    for fitness_class in classes:
        print(fitness_class)

def add_fitness_class():
    name = input("Enter the class name: ")
    trainer_id = input("Enter the trainer ID: ")
    date = datetime.today().strftime('%Y-%m-%d')
    start_time = input("Enter the start time (HH:MM): ")
    duration = input("Enter the duration (in minutes): ")
    FitnessClass.add_fitness_class(name, trainer_id, date, start_time, duration)
    print("Fitness class added successfully!")

def list_payments():
    payments = Payment.get_all_payments()
    for payment in payments:
        print(payment)

def add_payment():
    member_id = input("Enter the member's ID: ")
    amount = input("Enter the payment amount: ")
    date = datetime.today().strftime('%Y-%m-%d')
    Payment.add_payment(member_id, amount, date)
    print("Payment added successfully!")
