from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_planet import ModelPlanet
import graphene
import utils


# Create a generic class to mutualize description of planet attributes for both queries and mutations
class PlanetAttribute:
    name = graphene.String(description="Name of the planet.")
    rotation_period = graphene.String(description="Rotation period of the planet.")
    orbital_period = graphene.String(description="Orbital period of the planet.")
    diameter = graphene.String(description="Diameter of the planet.")
    climate = graphene.String(description="Climate period of the planet.")
    gravity = graphene.String(description="Gravity of the planet.")
    terrain = graphene.String(description="Terrain of the planet.")
    surface_water = graphene.String(description="Surface water of the planet.")
    population = graphene.String(description="Population of the planet.")
    url = graphene.String(description="URL of the planet in the Star Wars API.")


class Planet(SQLAlchemyObjectType):
    """Planet node."""

    class Meta:
        model = ModelPlanet
        interfaces = (graphene.relay.Node,)


class CreatePlanetInput(graphene.InputObjectType, PlanetAttribute):
    """Arguments to create a planet."""
    pass


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


class UpdatePlanetInput(graphene.InputObjectType, PlanetAttribute):
    """Arguments to update a planet."""
    id = graphene.ID(required=True, description="Global Id of the planet.")


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
