import os
import requests

from .constants import API_LIMIT, API_OFFEST
from src.exceptions.custom_exceptions import PokeAPIError



API_URL = os.getenv("API_URL")

def get_api_all_pokemons():

    # Get all pokemons
    params = {
        "limit": API_LIMIT,
        "offset": API_OFFEST,
    }
    url = f"{API_URL}/pokemon"
    response = call_endpoint(url, params)

    # Added id to the response because the original 
    # response has it in the url
    id = 0
    results = response['results']
    
    for result in results:
        id+=1
        result['id'] = id

    return response

def get_api_pokemon_by_id(id: int):

    params =  None
    url = f"{API_URL}/pokemon/{id}"
    response = call_endpoint(url, params)
    return response

def call_endpoint(url: str, params: dict):

    print(url)
    response = requests.get(url=url, params=params)
    if response.status_code != 200:
        raise PokeAPIError("Something failed in Poke API")
    
    return response.json()