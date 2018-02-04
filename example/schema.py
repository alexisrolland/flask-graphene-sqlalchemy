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


class Mutation(graphene.ObjectType):
    createPerson = schema_people.CreatePerson.Field()
    updatePerson = schema_people.UpdatePerson.Field()
    createPlanet = schema_planet.CreatePlanet.Field()
    updatePlanet = schema_planet.UpdatePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
