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
            # Extract planet id from url
            record['id'] = record['url'][record['url'].index('https://swapi.co/api/planets/')+29:-1]
            planet = model_planet.Planet(**record)
            database.db_session.add(planet)
        database.db_session.commit()

    log.info('Insert People data in database')
    with open('database/data/people.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            # Extract people and planet id from urls
            record['id'] = record['url'][record['url'].index('https://swapi.co/api/people/')+28:-1]
            record['homeworld'] = record['homeworld'][record['homeworld'].index('https://swapi.co/api/planets/')+29:-1]
            planet = model_people.People(**record)
            database.db_session.add(planet)
        database.db_session.commit()
