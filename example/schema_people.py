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
    name = graphene.String(required=True)
    height = graphene.String(default_value="unknown")
    mass = graphene.String(default_value="unknown")
    hair_color = graphene.String(default_value="unknown")
    skin_color = graphene.String(default_value="unknown")
    eye_color = graphene.String(default_value="unknown")
    birth_year = graphene.String(default_value="unknown")
    gender = graphene.String(default_value="unknown")
    planet_id = graphene.ID(default_value="unknown")
    url = graphene.String(default_value="unknown")


class CreatePerson(graphene.Mutation):
    """Create a person."""
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
    id = graphene.ID(required=True)
    name = graphene.String()
    height = graphene.String()
    mass = graphene.String()
    hair_color = graphene.String()
    skin_color = graphene.String()
    eye_color = graphene.String()
    birth_year = graphene.String()
    gender = graphene.String()
    planet_id = graphene.ID()
    url = graphene.String()


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
