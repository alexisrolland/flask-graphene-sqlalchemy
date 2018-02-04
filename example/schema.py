from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_planet
import schema_people


class Query(graphene.ObjectType):
    """Query objects for GraphQL API."""

    node = graphene.relay.Node.Field()
    people = graphene.relay.Node.Field(schema_people.People)
    peopleList = SQLAlchemyConnectionField(schema_people.People)
    planet = graphene.relay.Node.Field(schema_planet.Planet)
    planetList = SQLAlchemyConnectionField(schema_planet.Planet)


schema = graphene.Schema(query=Query)
