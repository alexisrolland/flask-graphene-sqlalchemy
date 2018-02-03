from ast import literal_eval
from model_people import ModelPeople
from model_planet import ModelPlanet
import base
import logging
import sys

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    log.info('Create database {}'.format(base.db_name))
    base.Base.metadata.create_all(base.engine)

    log.info('Insert Planet data in database')
    with open('data/planet.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            planet = ModelPlanet(**record)
            base.db_session.add(planet)
        base.db_session.commit()

    log.info('Insert People data in database')
    with open('data/people.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            planet = ModelPeople(**record)
            base.db_session.add(planet)
        base.db_session.commit()
