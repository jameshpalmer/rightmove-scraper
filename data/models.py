from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class Property(Base):
    """
    Represents a property on Rightmove
    """

    __tablename__ = "property"
    id = Column(Integer, primary_key=True)
    search_id = Column(Integer, ForeignKey("search.id"))
    url = Column(String)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    summary = Column(String)
    address = Column(String)
    longitude = Column(Numeric)
    latitude = Column(Numeric)
    price = Column(String)
    letting_agent = Column(String)

    search = relationship("Search", backref="properties")

    def __repr__(self) -> str:
        return f"<Property(id={self.id}, url={self.url}, bedrooms={self.bedrooms}, bathrooms={self.bathrooms}, summary={self.summary}, address={self.address}, longitude={self.longitude}, latitude={self.latitude}, price={self.price}, letting_agent={self.letting_agent})>"


class Search(Base):
    """
    Represents a Rightmove property search
    """

    __tablename__ = "search"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    notification_channel_id = Column(Integer, ForeignKey("notification_channel.id"))
    url = Column(String)

    notification_channels = relationship("NotificationChannel", backref="search")

    def __repr__(self) -> str:
        return f"<Search(id={self.id}, name={self.name}, notification_channel_id={self.notification_channel_id}, url={self.url})>"


class NotificationChannel(Base):
    """
    Represents a notify_run channel
    """

    __tablename__ = "notification_channel"
    id = Column(String, primary_key=True)
    all_members = Column(Boolean)

    def __repr__(self) -> str:
        return f"<NotificationChannel(id={self.id}, all_members={self.all_members})>"
