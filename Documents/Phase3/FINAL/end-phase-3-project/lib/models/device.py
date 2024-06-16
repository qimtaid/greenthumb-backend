from sqlalchemy import Column, Integer, String
from .base import Base

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Device(name={self.name})>"
