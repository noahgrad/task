from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from config.settings import HISTORY_PATH
import os
import shutil
import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def process_file(filepath, processing_funcs, history_dir=HISTORY_PATH):
    """
    Processes a file based on its type and moves it to the history folder.

    Parameters:
        filepath (str): The path of the file to process.
        processing_funcs (dict): A dictionary mapping file types to their respective processing functions.
    """
    if os.path.exists(filepath):
        for key, func in processing_funcs.items():
            logger.info(f"key {key} func {func}")
            if key in filepath:
                func(filepath)

        # Move the file to the history folder
        history_folder = history_dir
        if not os.path.exists(history_folder):
            os.makedirs(history_folder)
        shutil.move(filepath, f"{history_folder}/{filepath.split('/')[-1]}")
    else:
        logger.info(f"file {filepath} is not fully created yet")

class Watcher:
    """
    Watches a directory for file changes.
    """
    def __init__(self, directory_to_watch, processing_funcs):
        """
        Initialize the Watcher.

        Parameters:
            directory_to_watch (str): The directory to watch.
            processing_funcs (dict): A dictionary mapping file types to their respective processing functions.
        """
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.processing_funcs = processing_funcs  # Dictionary of processing functions
        self.observer = Observer()

    def process_existing_files(self):
        """
        Processes all existing files in the directory.
        """
        for filename in os.listdir(self.DIRECTORY_TO_WATCH):
            filepath = os.path.join(self.DIRECTORY_TO_WATCH, filename)
            process_file(filepath, self.processing_funcs)

    def run(self):
        """
        Start the directory watcher.
        """
        # Process existing files first
        self.process_existing_files()

        event_handler = Handler(self.processing_funcs)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

class Handler(FileSystemEventHandler):
    """
    Handles file system events.
    """
    def __init__(self, processing_funcs):
        """
        Initialize the Handler.

        Parameters:
            processing_funcs (dict): A dictionary mapping file types to their respective processing functions.
        """
        self.processing_funcs = processing_funcs

    def process(self, event):
        """
        Process a file system event.

        Parameters:
            event: The file system event to process.
        """
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print(f"Received created event - {event.src_path}")
            process_file(event.src_path, self.processing_funcs)

    def on_modified(self, event):
        """
        Handle a modified file event.

        Parameters:
            event: The file system event to process.
        """
        self.process(event)

    def on_created(self, event):
        """
        Handle a created file event.

        Parameters:
            event: The file system event to process.
        """
        self.process(event)
