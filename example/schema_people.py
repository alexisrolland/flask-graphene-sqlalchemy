from graphene_sqlalchemy import SQLAlchemyObjectType
from database.model_people import ModelPeople
import graphene


class People(SQLAlchemyObjectType):
    """People."""

    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node,)
