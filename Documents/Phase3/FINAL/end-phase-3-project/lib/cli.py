import argparse
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

def main():
    engine = setup_database()
    Session = sessionmaker(bind=engine)
    session = Session()

    parser = argparse.ArgumentParser(description="Energy Usage Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    log_parser = subparsers.add_parser("log", help="Log energy usage")
    log_parser.add_argument("--user", required=True, type=int, help="User ID")
    log_parser.add_argument("--device", required=True, type=int, help="Device ID")
    log_parser.add_argument("--usage", required=True, type=float, help="Energy usage")
    log_parser.add_argument("--unit", required=True, help="Unit of usage")

    report_parser = subparsers.add_parser("report", help="Generate usage report")

    args = parser.parse_args()

    if args.command == "log":
        user = session.query(User).filter_by(id=args.user).first()
        device = session.query(Device).filter_by(id=args.device).first()
        if user and device:
            usage = EnergyUsage(user_id=args.user, device_id=args.device, usage=args.usage, unit=args.unit)
            session.add(usage)
            session.commit()
            print(f"Logged {args.usage} {args.unit} for {device.name} by {user.name}")
        else:
            print("Invalid user or device ID")
    elif args.command == "report":
        report = {}
        usages = session.query(EnergyUsage).all()
        for usage in usages:
            device_name = usage.device.name
            if device_name not in report:
                report[device_name] = 0
            report[device_name] += usage.usage
        for device, total_usage in report.items():
            print(f"{device}: {total_usage} kWh")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
