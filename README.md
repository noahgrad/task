# Task Project

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Setting Up RQ](#setting-up-rq)
5. [How It Works](#how-it-works)
6. [Scalability](#scalability)
7. [Usage](#usage)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.x**: The project is written in Python and requires Python 3.x to run.
- **MySQL Database**: The project uses MySQL for database operations.
- **Redis**: The project uses Redis as an in-memory data store.
- **RQ (Redis Queue)**: Used for managing background tasks.
- **pip**: Make sure you have pip installed for package management.

## Installation

Follow these steps to get the project up and running:

1. **Clone the Repository**

    ```bash
    git clone https://github.com/noahgrad/task.git
    ```

2. **Navigate to the Project Directory**

    ```bash
    cd task
    ```

3. **Install Required Packages**

    ```bash
    pip install -r src/requirements.txt
    ```

## Configuration

1. **Database Settings**: Edit the `src/config/settings.py` file to configure your MySQL database settings.
2. **Redis Settings**: Make sure Redis is running on the specified port in your configuration.
3. **Environment Variables**: Run `utils/prepare_env.py` to set up the necessary environment variables.

## Setting Up RQ

1. **Start Redis Server**: If you haven't already, start your Redis server.

    ```bash
    redis-server
    ```

2. **Run RQ Worker**: Navigate to the project directory and run the following command to start an RQ worker.

    ```bash
    rq worker
    ```

## How It Works

- **Database Manager (`src/db_manager.py`)**: Manages database operations.
- **File Watcher (`src/file_watcher.py`)**: Watches for file changes.
- **Queue Manager (`src/queue_manager.py`)**: Manages task queues using RQ.
- **Task Runner (`src/task_runner.py`)**: Executes tasks.
- **Worker Function (`src/worker_function_my_sql.py`)**: Worker function for MySQL operations.

## Scalability

Your implementation is designed for scalability for the following reasons:

- **Modular Design**: Each component (Database Manager, File Watcher, Queue Manager, etc.) is designed to function independently, making it easier to scale each component as needed.
  
- **Asynchronous Task Handling**: Using RQ for background tasks allows the system to handle more tasks concurrently, improving throughput.

- **Distributed Computing**: With Redis and RQ, tasks can be distributed across multiple workers and even multiple machines, allowing for horizontal scaling.

## Usage

Run the following command to start the project:

```bash
python src/task_runner.py

