from graphene_sqlalchemy import SQLAlchemyObjectType
from database.model_planet import ModelPlanet
import graphene


class Planet(SQLAlchemyObjectType):
    """Planet."""

    class Meta:
        model = ModelPlanet
        interfaces = (graphene.relay.Node,)
