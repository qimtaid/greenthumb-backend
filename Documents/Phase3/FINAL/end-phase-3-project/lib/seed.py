from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.user import User
from models.device import Device
from models.energy_usage import EnergyUsage

DATABASE_URL = 'sqlite:///energy_usage.db'

def setup_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    return engine

def seed_data():
    engine = setup_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    user1 = User(name="John Doe", email="john@example.com")
    user2 = User(name="Jane Smith", email="jane@example.com")
    device1 = Device(name="Refrigerator")
    device2 = Device(name="Air Conditioner")
    device3 = Device(name="Washing Machine")
    device4 = Device(name="Television")

    session.add_all([user1, user2, device1, device2, device3, device4])
    session.commit()

    usage1 = EnergyUsage(user_id=user1.id, device_id=device1.id, usage=0.8, unit="kWh")
    usage2 = EnergyUsage(user_id=user1.id, device_id=device2.id, usage=3.5, unit="kWh")
    usage3 = EnergyUsage(user_id=user2.id, device_id=device3.id, usage=1.2, unit="kWh")
    usage4 = EnergyUsage(user_id=user2.id, device_id=device4.id, usage=0.2, unit="kWh")

    session.add_all([usage1, usage2, usage3, usage4])
    session.commit()

    print("Seed data added.")

if __name__ == "__main__":
    seed_data()
