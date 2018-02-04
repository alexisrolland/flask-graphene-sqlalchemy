from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_planet import ModelPlanet
import graphene
import utils


class Planet(SQLAlchemyObjectType):
    """Planet."""

    class Meta:
        model = ModelPlanet
        interfaces = (graphene.relay.Node,)


class CreatePlanetInput(graphene.InputObjectType):
    """Arguments to create a planet."""
    name = graphene.String(required=True)
    rotation_period = graphene.String(default_value="unknown")
    orbital_period = graphene.String(default_value="unknown")
    diameter = graphene.String(default_value="unknown")
    climate = graphene.String(default_value="unknown")
    gravity = graphene.String(default_value="unknown")
    terrain = graphene.String(default_value="unknown")
    surface_water = graphene.String(default_value="unknown")
    population = graphene.String(default_value="unknown")
    url = graphene.String(default_value="unknown")


class CreatePlanet(graphene.Mutation):
    """Create a planet."""
    planet = graphene.Field(lambda: Planet)

    class Arguments:
        input = CreatePlanetInput(required=True)

    def mutate(self, info, input):
        """Create a planet."""
        data = utils.input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        planet = ModelPlanet(**data)
        db_session.add(planet)
        db_session.commit()

        return CreatePlanet(planet=planet)


class UpdatePlanetInput(graphene.InputObjectType):
    """Arguments to update a planet."""
    id = graphene.ID(required=True)
    name = graphene.String()
    rotation_period = graphene.String()
    orbital_period = graphene.String()
    diameter = graphene.String()
    climate = graphene.String()
    gravity = graphene.String()
    terrain = graphene.String()
    surface_water = graphene.String()
    population = graphene.String()
    url = graphene.String()


class UpdatePlanet(graphene.Mutation):
    """Update a planet."""
    planet = graphene.Field(lambda: Planet)

    class Arguments:
        input = UpdatePlanetInput(required=True)

    def mutate(self, info, input):
        """Update a planet."""
        data = utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        planet = db_session.query(ModelPlanet).filter_by(id=data['id'])
        planet.update(data)
        db_session.commit()
        planet = db_session.query(ModelPlanet).filter_by(id=data['id']).first()

        return UpdatePlanet(planet=planet)
