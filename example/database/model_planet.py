from .base import Base
from .model_people import ModelPeople
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class ModelPlanet(Base):
    """Planet model."""

    __tablename__ = 'planet'

    id = Column('id', Integer, primary_key=True, doc="Id of the person.")
    name = Column('name', String, doc="Name of the planet.")
    rotation_period = Column('rotation_period', String, doc="Rotation period of the planet.")
    orbital_period = Column('orbital_period', String, doc="Orbital period of the planet.")
    diameter = Column('diameter', String, doc="Diameter of the planet.")
    climate = Column('climate', String, doc="Climate period of the planet.")
    gravity = Column('gravity', String, doc="Gravity of the planet.")
    terrain = Column('terrain', String, doc="Terrain of the planet.")
    surface_water = Column('surface_water', String, doc="Surface water of the planet.")
    population = Column('population', String, doc="Population of the planet.")
    created = Column('created', String, doc="Record created date.")
    edited = Column('edited', String, doc="Record last updated date.")
    url = Column('url', String, doc="URL of the planet in the Star Wars API.")

    peopleList = relationship(ModelPeople, backref='planet')
