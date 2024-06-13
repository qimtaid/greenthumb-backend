from models.member import Member
from models.trainer import Trainer
from models.attendance import Attendance
from models.fitness_class import FitnessClass
from models.payment import Payment
from datetime import datetime

def seed_database():
    # Seed members
    #Member.create_table()
    #Member.add_member("John Doe", "john@example.com", "Male", "28", datetime.today().strftime('%Y-%m-%d'), "0111222333")
    #Member.add_member("Jane Smith", "jane@example.com", "Female", "32", datetime.today().strftime('%Y-%m-%d'), "0714555666")
    #Member.add_member("Alice Johnson", "alice@example.com", "Female", "25", datetime.today().strftime('%Y-%m-%d'), "0200333444")

    

    # Seed attendance records
    #Attendance.create_table()
    #Attendance.add_attendance(1, 1, "2024-06-01")
    #Attendance.add_attendance(2, 2, "2024-06-02")
    #Attendance.add_attendance(3, 3, "2024-06-03")
    
    # Seed payments
    #Payment.create_table()
    #Payment.add_payment(1, 50.0, "2024-06-01", "cash")
    #Payment.add_payment(2, 75.0, "2024-06-02", "Credit card")
    #Payment.add_payment(3, 100.0, "2024-06-03", "M-Pesa")
    
    # Seed trainers
    Trainer.create_table()
    Trainer.add_trainer("Mike Tyson", "mike@example.com", "30","Male", "Professional Boxer", datetime.today().strftime('%Y-%m-%d'), "0100200300")
    Trainer.add_trainer("Serena Williams", "serena@example.com", "27", "Female", "Tennis Champion", datetime.today().strftime('%Y-%m-%d'), "0101202303")
    Trainer.add_trainer("Usain Bolt", "usain@example.com", "Male", "25", "Sprinter", datetime.today().strftime('%Y-%m-%d'), "0733444555")

    # Seed fitness classes
    #FitnessClass.create_table()
    #FitnessClass.add_fitness_class("Yoga", 1, "2024-06-01", "08:00", 60)
    #FitnessClass.add_fitness_class("Pilates", 2, "2024-06-02", "09:00", 60)
    #FitnessClass.add_fitness_class("CrossFit", 3, "2024-06-03", "10:00", 60)
    
    

if __name__ == "__main__":
    seed_database()
