from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    cuisine_style = Column(String, nullable=False)
    seats_nb = Column(Integer)
