from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_planet
import schema_people


class Query(graphene.ObjectType):
    """Nodes which can be queried by this API."""
    node = graphene.relay.Node.Field()

    # People
    people = graphene.relay.Node.Field(schema_people.People)
    peopleList = SQLAlchemyConnectionField(schema_people.People)

    # Planet
    planet = graphene.relay.Node.Field(schema_planet.Planet)
    planetList = SQLAlchemyConnectionField(schema_planet.Planet)


class Mutation(graphene.ObjectType):
    """Mutations which can be performed by this API."""
    # Person mutation
    createPerson = schema_people.CreatePerson.Field()
    updatePerson = schema_people.UpdatePerson.Field()

    # Planet mutations
    createPlanet = schema_planet.CreatePlanet.Field()
    updatePlanet = schema_planet.UpdatePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
