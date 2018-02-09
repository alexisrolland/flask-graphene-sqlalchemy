from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_people import ModelPeople
import graphene
import utils


class People(SQLAlchemyObjectType):
    """People node."""

    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node,)


class CreatePersonInput(graphene.InputObjectType):
    """Arguments to create a person."""

    name = graphene.String(required=True, description="Name of the person to be created.")
    height = graphene.String(default_value="unknown", description="Height of the person to be created.")
    mass = graphene.String(default_value="unknown", description="Mass of the person to be created.")
    hair_color = graphene.String(default_value="unknown", description="Hair color of the person to be created.")
    skin_color = graphene.String(default_value="unknown", description="Skin color of the person to be created.")
    eye_color = graphene.String(default_value="unknown", description="Eye color of the person to be created.")
    birth_year = graphene.String(default_value="unknown", description="Birth year of the person to be created.")
    gender = graphene.String(default_value="unknown", description="Gender of the person to be created.")
    planet_id = graphene.ID(default_value="unknown", description="Global Id of the planet from which the person to be created comes from.")
    url = graphene.String(default_value="unknown", description="URL of the person in the Star Wars API.")


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


class UpdatePersonInput(graphene.InputObjectType):
    """Arguments to update a person."""
    id = graphene.ID(required=True, description="Global Id of the person to be updated.")
    name = graphene.String(description="New value for the name of the person to be updated.")
    height = graphene.String(description="New value for the height of the person to be updated.")
    mass = graphene.String(description="New value for the mass of the person to be updated.")
    hair_color = graphene.String(description="New value for the hair color of the person to be updated.")
    skin_color = graphene.String(description="New value for the skin color of the person to be updated.")
    eye_color = graphene.String(description="New value for the eye color of the person to be updated.")
    birth_year = graphene.String(description="New value for the birth year of the person to be updated.")
    gender = graphene.String(description="New value for the gender of the person to be updated.")
    planet_id = graphene.ID(description="New global Id of the planet from which the person to be updated comes from.")
    url = graphene.String(description="New value for the Star Wars API URL of the person to be updated.")


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
