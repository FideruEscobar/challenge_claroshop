from flask import Blueprint, make_response
from flask_pydantic import validate

from src.utils.util import output_json
from src.services.pokemons_service import (
    get_api_all_pokemons,
    get_api_pokemon_by_id
)


pokemonsRouting = Blueprint('pokemonsRouting', __name__)


@pokemonsRouting.route('/')
def health_resource():
    return output_json({"message": "Test API"}), 200

@pokemonsRouting.route('/pokemon/<id>', methods=["GET"])
@validate()
def get_pokemon_by_id(id: int):
    response = get_api_pokemon_by_id(id)
    return make_response(response, 200)

@pokemonsRouting.route('/pokemons', methods=["GET"])
def get_all_pokemons():
    response = get_api_all_pokemons()
    return make_response(response, 200)
