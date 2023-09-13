import json, os
import subprocess
import atexit
from lemonade_task.file_watcher import Watcher  # Import the Watcher class
from lemonade_task.queue_manager import QueueManager
from dotenv import load_dotenv
load_dotenv()
from lemonade_task.config.settings import SRC_PATH, LOG_DIR
from apscheduler.schedulers.background import BackgroundScheduler
from lemonade_task.db_manager import DBManager



import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

qm = QueueManager()

def parse_and_enqueue_vehicle_events(file_path):
    """
    Parse and enqueue vehicle events from a file.

    Parameters:
        file_path (str): The path of the file to parse.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    for event in data['vehicle_events']:
        logger.info(f"vehicle_events enquing {event}")
        qm.enqueue_event(event)

def parse_and_enqueue_vehicle_status(file_path):
    """
    Parse and enqueue vehicle status from a file.

    Parameters:
        file_path (str): The path of the file to parse.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    for status in data['vehicle_status']:
        logger.info(f"vehicle_status enquing {status}")
        qm.enqueue_status(status)

def terminate_workers(workers):
    for worker in workers:
        worker.terminate()

def main():
    db = DBManager()

    # create the tables if needed
    db.create_tables()

    # Update the daily summary table based on historical data
    db.update_daily_summary()

    # Schedule the update_daily_summary to run every day
    scheduler = BackgroundScheduler()

    scheduler.add_job(db.update_daily_summary, 'interval', days=1)
    scheduler.start()

    processing_funcs = {
        'vehicle_events': parse_and_enqueue_vehicle_events,
        'vehicle_status': parse_and_enqueue_vehicle_status
    }
    # Start RQ Workers for 'vehicle_events' and 'vehicle_status' queues
    script_directory = os.path.dirname(os.path.abspath(__file__))
    workers = []
    for name in processing_funcs:
        with open(f"{LOG_DIR}/worker_output_{name}.log", "w+") as f:
            workers.append(
                subprocess.Popen(["rq", "worker", name], stdout=f, stderr=f, cwd=script_directory, env=os.environ))

    # Register the termination function to be called when the script exits
    atexit.register(terminate_workers, workers)

    watcher = Watcher(SRC_PATH, processing_funcs)
    watcher.run()


if __name__ == '__main__':
    main()




