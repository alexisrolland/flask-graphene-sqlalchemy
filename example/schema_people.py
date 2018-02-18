from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_people import ModelPeople
import graphene
import utils


# Create a generic class to mutualize description of people attributes for both queries and mutations
class PeopleAttribute:
    name = graphene.String(description="Name of the person.")
    height = graphene.String(description="Height of the person.")
    mass = graphene.String(description="Mass of the person.")
    hair_color = graphene.String(description="Hair color of the person.")
    skin_color = graphene.String(description="Skin color of the person.")
    eye_color = graphene.String(description="Eye color of the person.")
    birth_year = graphene.String(description="Birth year of the person.")
    gender = graphene.String(description="Gender of the person.")
    planet_id = graphene.ID(description="Global Id of the planet from which the person comes from.")
    url = graphene.String(description="URL of the person in the Star Wars API.")


class People(SQLAlchemyObjectType):
    """People node."""

    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node,)


class CreatePersonInput(graphene.InputObjectType, PeopleAttribute):
    """Arguments to create a person."""
    pass


class CreatePerson(graphene.Mutation):
    """Mutation to create a person."""
    person = graphene.Field(lambda: People, description="Person created by this mutation.")

    class Arguments:
        input = CreatePersonInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        person = ModelPeople(**data)
        db_session.add(person)
        db_session.commit()

        return CreatePerson(person=person)


class UpdatePersonInput(graphene.InputObjectType, PeopleAttribute):
    """Arguments to update a person."""
    id = graphene.ID(required=True, description="Global Id of the person.")


class UpdatePerson(graphene.Mutation):
    """Update a person."""
    person = graphene.Field(lambda: People, description="Person updated by this mutation.")

    class Arguments:
        input = UpdatePersonInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        person = db_session.query(ModelPeople).filter_by(id=data['id'])
        person.update(data)
        db_session.commit()
        person = db_session.query(ModelPeople).filter_by(id=data['id']).first()

        return UpdatePerson(person=person)
