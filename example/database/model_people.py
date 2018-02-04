from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelPeople(Base):
    """People model."""

    __tablename__ = 'people'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    height = Column('height', String)
    mass = Column('mass', String)
    hair_color = Column('hair_color', String)
    skin_color = Column('skin_color', String)
    eye_color = Column('eye_color', String)
    birth_year = Column('birth_year', String)
    gender = Column('gender', String)
    planet_id = Column('planet_id', Integer, ForeignKey('planet.id'))
    created = Column('created', String)
    edited = Column('edited', String)
    url = Column('url', String)
