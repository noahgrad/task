import os

# Database settings
DB_USERNAME = os.environ.get('DB_USERNAME', 'root')
DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', 3307)
DB_NAME = os.environ.get('DB_NAME', 'vehicles')

# Redis settings
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)

#SRC_PATH
SRC_PATH = os.environ.get('SRC_PATH', '/Users/noa.gradovitch/lemonade/lemonade_task/inbound_folder')

#HISTORY_PATH
HISTORY_PATH = os.environ.get('SRC_PATH', '/Users/noa.gradovitch/lemonade/lemonade_task/history_folder')

#LOG DIR
LOG_DIR = os.environ.get('LOG_DIR', '/tmp/')