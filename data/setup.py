from .database import session
from .models import Property, Search, NotificationChannel
from notify_run import Notify
import pandas as pd


def create_tables():
    """
    Creates the tables in the database if they don't already exist.
    """
    Property.__table__.create(session.bind, checkfirst=True)
    Search.__table__.create(session.bind, checkfirst=True)
    NotificationChannel.__table__.create(session.bind, checkfirst=True)


def get_notify() -> tuple[Notify, Notify]:
    """
    Returns a tuple of Notify objects, one for single channel and one for double channel.
    """
    double_channel_id = "4M6NcNZZwZr6slfw1433"
    double_notify = NotificationChannel(name="double", id=double_channel_id)
    session.add(double_notify)
    session.commit()


def search_setup():
    """
    Sets up the searches in the database.
    """
    Search.__table__.drop(session.bind, checkfirst=True)
    Search.__table__.create(session.bind, checkfirst=True)
    search_df = pd.read_csv("data/input/searches.csv")
    for _, row in search_df.iterrows():
        notification_channel_id = row["Channel Id"]
        if session.query(NotificationChannel).get(notification_channel_id) is None:
            notification_channel = NotificationChannel(
                id=notification_channel_id, all_members=True
            )
            session.add(notification_channel)
            session.commit()

        search = Search(
            name=row["Name"],
            notification_channel_id=notification_channel_id,
            url=row["Url"],
        )
        session.add(search)
