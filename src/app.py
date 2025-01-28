"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from userservice import UserService
from planetservice import PlanetServise
from peopleservice import PeopleService
from favoriteservice import FavoriteService
#from models import Person



app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

user_service = UserService()
planet_service = PlanetServise(id)
people_service = PeopleService(id)
favorite_service = FavoriteService()

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_users():
    user = user_service.get_list()
    return jsonify(user), 200

@app.route('/user/favorites', methods=['GET'])
def get_favorites_list():
    favorite_list = favorite_service.get_list()
    return jsonify(favorite_list), 200

@app.route('/planets', methods=['GET'])
def planets_list():
    planet_list = planet_service.get_list()
    return jsonify(planet_list), 200

@app.route('/planets/<int:id>', methods=['GET'])
def planet_by_id(id):
    planet = planet_service.get_list_byId(id)
    return jsonify(planet), 200

@app.route('/people', methods=['GET'])
def people_list():
    person_list = people_service.get_list()
    return jsonify(person_list), 200

@app.route('/people/<int:id>', methods=['GET'])
def people_by_id(id):
    person = people_service.get_list_byId(id)
    return jsonify(person), 200

@app.route('/user/favorites/planets', methods=['POST'])
def add_favoritePlanets():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/favorites/people/<int:id>', methods=['POST'])
def add_favoritePeople():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/user/favorites/planets/<int:id>', methods=['DELETE'])
def remove_favoritePlanets():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/user/favorites/people/<int:id>', methods=['DELETE'])
def remove_favoritePeople():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
