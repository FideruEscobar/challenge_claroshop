import json
import os
from src.utils.util import open_json

def mock_call_endpoint_get_pokemon(url: str, params: dict):

    current_dir = os.path.dirname(__file__)
    return open_json(current_dir, 'mock_pokemon.json')
        
def mock_call_endpoint_all_pokemons(url: str, params: dict):

    current_dir = os.path.dirname(__file__)
    return open_json(current_dir, 'mock_all_pokemons.json')
