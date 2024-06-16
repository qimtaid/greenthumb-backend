from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base
from .user import User
from .device import Device

class EnergyUsage(Base):
    __tablename__ = 'energy_usages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    usage = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", back_populates="energy_usages")
    device = relationship("Device", back_populates="energy_usages")

    def __repr__(self):
        return f"<EnergyUsage(user_id={self.user_id}, device_id={self.device_id}, usage={self.usage}, unit={self.unit}, timestamp={self.timestamp})>"

User.energy_usages = relationship("EnergyUsage", order_by=EnergyUsage.id, back_populates="user")
Device.energy_usages = relationship("EnergyUsage", order_by=EnergyUsage.id, back_populates="device")
