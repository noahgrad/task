from redis import Redis
from rq import Queue
from config import settings
from worker_function_my_sql import insert_vehicle_status, insert_vehicle_event
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
class QueueManager:
    """
    Manages Redis queues.
    """
    def __init__(self):
        self.redis_conn = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        self.event_queue = Queue('vehicle_events', connection=self.redis_conn)
        self.status_queue = Queue('vehicle_status', connection=self.redis_conn)

    def enqueue_event(self, event):
        """
        Enqueues a new event.
        """
        logger.info(f"sending {event} to event_queue")
        self.event_queue.enqueue(insert_vehicle_event, event)

    def enqueue_status(self, status):
        """
        Enqueues a new status.
        """
        logger.info(f"sending {status} to status_queue")
        self.status_queue.enqueue(insert_vehicle_status, status)
