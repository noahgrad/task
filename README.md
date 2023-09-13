# Lemonade Task Project

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Scalability](#scalability)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [File Structure](#file-structure)
8. [Running Tests](#running-tests)
9. [Creating the Package](#creating-the-package)
10. [Usage](#usage)


---

## Overview

The Lemonade Task Project is a Python-based solution designed for efficient and scalable task management. It leverages Redis, RQ (Redis Queue), and MySQL for robust, distributed task handling.

---

## Features

- **File Watcher**: Monitors a directory for file changes.
- **Queue Manager**: Manages tasks in a Redis queue.
- **Database Manager**: Handles MySQL database operations.

---

## Scalability

### Why is it Scalable?

1. **Distributed Task Queue**: Utilizes RQ and Redis for distributing tasks across multiple workers.
2. **Asynchronous Operations**: Enables asynchronous task execution.
3. **Modular Design**: Independent, scalable components.

---

## Prerequisites

### Software Requirements

- Python 3.x
- Redis server
- RQ (Redis Queue)
- MySQL server

### Hardware Requirements

- Minimum 2 GB RAM
- Minimum 10 GB disk space

---

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/noahgrad/task.git
    ```

2. **Navigate to Project Directory**

    ```bash
    cd task
    ```

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install Development Requirements (Optional)**

    ```bash
    pip install -r requirements-dev.txt
    ```

5. **Make sure redis server is running**
6. **make sure mysql is running and setting are updated.**
---

## Configuration

1. **Redis Configuration**: Update Redis server details in `src/lemonade_task/config/settings.py`.
2. **Database Configuration**: Update MySQL configurations in `src/lemonade_task/config/settings.py`.

---

## File Structure

### `src/lemonade_task` Directory

- `db_manager.py`: Manages MySQL database operations.
- `file_watcher.py`: Watches a directory for file changes.
     - hanlde files that are alredy in the directory and new files that are coming
     - for each file: read it and send each event to the matching queue
     - move the file after processing to history directory
- `models.py`: Defines the data models.
- `queue_manager.py`: Manages the Redis queue.
- `task_runner.py`: Entry point for running tasks.
     -  create database tables
     -  update last event summary history table
     -  start the scheduler for summary
     -  start the watcher that watch the inbound directory
- `worker_function_my_sql.py`: Worker functions for MySQL operations (insert into the tables).

### `config` Sub-directory

- `settings.py`: Contains configuration settings like Redis and MySQL details.

### `tests` Directory

- `test_file_watcher.py`: Tests for file watcher functionality.

### `utils` Directory

- `prepare_env.py`: Utility script for preparing the environment.

---

## Running Tests

1. **Navigate to Project Directory**
2. **Run Tests**

    ```bash
    pytest tests/
    ```

---

## Creating the Package

1. **Navigate to Project Directory**
2. **Create Source Distribution**

    ```bash
    python setup.py sdist
    ```

---

## Usage

```bash
pip install task_project-0.1.0.tar.gz
```

After installing the package, use the `task_runner` command to start:

```bash
task_runner

