from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mysql.connector import OperationalError
from lemonade_task.config import settings
from lemonade_task.models import VehicleEvents, DailySummary, Base
from sqlalchemy import func


class DBManager:
    """
    Manages database connections and operations.
    """
    def __init__(self):
        self.engine = create_engine(
            f'mysql+mysqlconnector://{settings.DB_USERNAME}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}',
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=1800,
        )
        self.Session = sessionmaker(bind=self.engine)
        self.MAX_RETRIES = 3

    def perform_commit(self, new_obj):
        """
        Commits a new object to the database with retry logic.
        """
        session = self.Session()
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                session.add(new_obj)
                session.commit()
                break
            except OperationalError:
                print("MySQL Connection not available. Retrying...")
                session.rollback()
                retries += 1
            except Exception as e:
                session.rollback()
                print(f"Error: {e}")
                break
        if retries >= self.MAX_RETRIES:
            print("Max retries reached. Exiting.")
        session.close()

    def update_daily_summary(self):
        """
        Updates the daily summary table based on the events table.
        """
        session = self.Session()
        try:
            query = session.query(
                VehicleEvents.vehicle_id,
                func.date(VehicleEvents.event_time).label('day'),
                func.max(VehicleEvents.event_time).label('last_event_time'),
                VehicleEvents.event_type
            ).group_by(
                VehicleEvents.vehicle_id,
                func.date(VehicleEvents.event_time),
                VehicleEvents.event_type
            )

            for row in query:
                summary = DailySummary(
                    vehicle_id=row.vehicle_id,
                    day=row.day,
                    last_event_time=row.last_event_time,
                    last_event_type=row.event_type
                )
                session.merge(summary)

            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error: {e}")
        finally:
            session.close()

    def create_tables(self):
        Base.metadata.create_all(self.engine)