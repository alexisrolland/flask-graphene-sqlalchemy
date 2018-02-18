from .base import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class ModelPeople(Base):
    """People model."""

    __tablename__ = 'people'

    id = Column('id', Integer, primary_key=True, doc="Id of the person.")
    name = Column('name', String, doc="Name of the person.")
    height = Column('height', String, doc="Height of the person.")
    mass = Column('mass', String, doc="Mass of the person.")
    hair_color = Column('hair_color', String, doc="Hair color of the person.")
    skin_color = Column('skin_color', String, doc="Skin color of the person.")
    eye_color = Column('eye_color', String, doc="Eye color of the person.")
    birth_year = Column('birth_year', String, doc="Birth year of the person.")
    gender = Column('gender', String, doc="Gender of the person.")
    planet_id = Column('planet_id', Integer, ForeignKey('planet.id'), doc="Id of the planet from which the person comes from.")
    created = Column('created', String, doc="Record created date.")
    edited = Column('edited', String, doc="Record last updated date.")
    url = Column('url', String, doc="URL of the person in the Star Wars API.")
