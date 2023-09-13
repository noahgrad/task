from setuptools import setup, find_packages

setup(
    name='task_project',
    version='0.1.0',
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        'python-dotenv',
        'watchdog',
        'redis',
        'rq',
        'sqlalchemy',
        'mysql-connector-python',
        'apscheduler'
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'task_runner=lemonade_task.task_runner:main',
            # Add other entry points here
        ],
    },
)
