from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_planet import ModelPlanet
import graphene
import utils


class Planet(SQLAlchemyObjectType):
    """Planet node."""

    class Meta:
        model = ModelPlanet
        interfaces = (graphene.relay.Node,)


class CreatePlanetInput(graphene.InputObjectType):
    """Arguments to create a planet."""
    name = graphene.String(required=True, description="Name of the planet to be created.")
    rotation_period = graphene.String(default_value="unknown", description="Rotation period of the planet to be created.")
    orbital_period = graphene.String(default_value="unknown", description="Orbital period of the planet to be created.")
    diameter = graphene.String(default_value="unknown", description="Diameter of the planet to be created.")
    climate = graphene.String(default_value="unknown", description="Climate period of the planet to be created.")
    gravity = graphene.String(default_value="unknown", description="Gravity of the planet to be created.")
    terrain = graphene.String(default_value="unknown", description="Terrain of the planet to be created.")
    surface_water = graphene.String(default_value="unknown", description="Surface water of the planet to be created.")
    population = graphene.String(default_value="unknown", description="Population of the planet to be created.")
    url = graphene.String(default_value="unknown", description="URL of the planet in the Star Wars API.")


class CreatePlanet(graphene.Mutation):
    """Create a planet."""
    planet = graphene.Field(lambda: Planet, description="Planet created by this mutation.")

    class Arguments:
        input = CreatePlanetInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        planet = ModelPlanet(**data)
        db_session.add(planet)
        db_session.commit()

        return CreatePlanet(planet=planet)


class UpdatePlanetInput(graphene.InputObjectType):
    """Arguments to update a planet."""
    id = graphene.ID(required=True, description="Global Id of the planet to be updated.")
    name = graphene.String(description="New value for the name of the planet to be updated.")
    rotation_period = graphene.String(description="New value for the rotation period of the planet to be updated.")
    orbital_period = graphene.String(description="New value for the orbital period of the planet to be updated.")
    diameter = graphene.String(description="New value for the diameter of the planet to be updated.")
    climate = graphene.String(description="New value for the climate of the planet to be updated.")
    gravity = graphene.String(description="New value for the gravity of the planet to be updated.")
    terrain = graphene.String(description="New value for the terrain of the planet to be updated.")
    surface_water = graphene.String(description="New value for the surface water of the planet to be updated.")
    population = graphene.String(description="New value for the population of the planet to be updated.")
    url = graphene.String(description="New value for the Star Wars API URL of the planet to be updated.")


class UpdatePlanet(graphene.Mutation):
    """Update a planet."""
    planet = graphene.Field(lambda: Planet, description="Planet updated by this mutation.")

    class Arguments:
        input = UpdatePlanetInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        planet = db_session.query(ModelPlanet).filter_by(id=data['id'])
        planet.update(data)
        db_session.commit()
        planet = db_session.query(ModelPlanet).filter_by(id=data['id']).first()

        return UpdatePlanet(planet=planet)
