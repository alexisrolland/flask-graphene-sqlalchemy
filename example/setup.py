from ast import literal_eval
from database import database
from database import model_people
from database import model_planet
import logging
import sys

# Load logging configuration
log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    log.info('Create database {}'.format(database.db_name))
    database.Base.metadata.create_all(database.engine)

    log.info('Insert Planet data in database')
    with open('database/data/planet.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            planet = model_planet.Planet(**record)
            database.db_session.add(planet)
        database.db_session.commit()

    log.info('Insert People data in database')
    with open('database/data/people.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            planet = model_people.People(**record)
            database.db_session.add(planet)
        database.db_session.commit()
