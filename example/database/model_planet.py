from .database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Planet(Base):
    """Planet model."""

    __tablename__ = 'planet'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    rotation_period = Column('rotation_period', Integer)
    orbital_period = Column('orbital_period', Integer)
    diameter = Column('diameter', Integer)
    climate = Column('climate', String)
    gravity = Column('gravity', String)
    terrain = Column('terrain', String)
    surface_water = Column('surface_water', Integer)
    population = Column('population', Integer)
    created = Column('created', String)
    edited = Column('edited', String)
    url = Column('url', String)

    peoples = relationship('People', backref='planet')
