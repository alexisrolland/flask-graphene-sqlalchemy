from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class People(Base):
    """People model."""

    __tablename__ = 'people'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    height = Column('height', Integer)
    mass = Column('mass', Integer)
    hair_color = Column('hair_color', String)
    skin_color = Column('skin_color', String)
    eye_color = Column('eye_color', String)
    birth_year = Column('birth_year', String)
    gender = Column('gender', String)
    homeworld = Column('homeworld', Integer, ForeignKey('planet.id'))
    created = Column('created', String)
    edited = Column('edited', String)
    url = Column('url', String)
