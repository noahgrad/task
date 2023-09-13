from lemonade_task.db_manager import DBManager
from lemonade_task.models import VehicleEvents, VehicleStatus
import datetime, json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

db = DBManager()

def insert_vehicle_event(event):
    new_event = VehicleEvents(
        vehicle_id=event['vehicle_id'],
        event_time=datetime.datetime.fromisoformat(event['event_time'].replace('Z', '+00:00')),
        event_source=event['event_source'],
        event_type=event['event_type'],
        event_value=event['event_value'],
        event_extra_data=json.dumps(event.get('event_extra_data', {}))
    )
    logger.info(f"going to insert to db event {new_event}")
    db.perform_commit(new_obj=new_event)


def insert_vehicle_status(status):
    new_status = VehicleStatus(
        vehicle_id=status['vehicle_id'],
        report_time=datetime.datetime.fromisoformat(status['report_time'].replace('Z', '+00:00')),
        status_source=status['status_source'],
        status=status['status']
    )
    logger.info(f"going to insert to db {new_status}")
    db.perform_commit(new_obj=new_status)
