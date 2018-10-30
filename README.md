# Flask-Graphene-SQLAlchemy
The purpose of this repository is to provide a project template to build a **GraphQL API in Python**. Its content has been largely inspired by the references below but code has been modified and enriched to provide a more complete API and a more scalable architecture.

# Tutorial
The [Github Wiki](https://github.com/alexisrolland/flask-graphene-sqlalchemy/wiki) provides detailed design intentions in a step by step tutorial.

# References
* [Graphene-SQLAlchemy](http://docs.graphene-python.org/projects/sqlalchemy/en/latest)
* [Flask-Graphene-SQLAlchemy](https://github.com/Getmrahul/Flask-Graphene-SQLAlchemy)
* [Star Wars API](https://swapi.co)

# Requirements
This project has been developed on **Linux Ubuntu** with **Python 3.5**. It is using the following third party packages. To install them, open a terminal window, change directory to the project folder and execute the following command:

`$ pip3 install -r requirements.txt`

The following Python packages will be installed:
* [flask](http://flask.pocoo.org) (0.12.3)
* [flask-graphql](https://pypi.python.org/pypi/Flask-GraphQL) (1.4.1)
* [graphene](http://graphene-python.org) (2.0.0)
* [graphene-sqlalchemy](https://pypi.python.org/pypi/graphene-sqlalchemy/2.0.0) (2.0.0)
* [nose2](http://nose2.readthedocs.io/en/latest/) (0.7.4) - Used for running tests
* [requests](http://docs.python-requests.org/en/master/) (2.20.0) - Used for running tests
* [sqlalchemy](https://www.sqlalchemy.org) (1.1.14)

# Run Test Cases
To execute all test cases, change directory to the project root folder and execute the following command:

$ nose2 -v
