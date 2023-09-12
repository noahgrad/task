from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class VehicleEvents(Base):
    __tablename__ = 'vehicle_events'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String(255))
    event_time = Column(DateTime)
    event_source = Column(String(255))
    event_type = Column(String(255))
    event_value = Column(String(255))
    event_extra_data = Column(String(255))

class VehicleStatus(Base):
    __tablename__ = 'vehicle_status'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String(255))
    report_time = Column(DateTime)
    status_source = Column(String(255))
    status = Column(String(255))

class DailySummary(Base):
    __tablename__ = 'daily_summary'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(String(255))
    day = Column(Date)
    last_event_time = Column(DateTime)
    last_event_type = Column(String(255))
