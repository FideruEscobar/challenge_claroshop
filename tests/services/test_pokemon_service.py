from src.services.pokemons_service import call_endpoint


def test_call_endpoint():

    id = 1
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = call_endpoint(url, params=None)

    assert isinstance(response, dict)
   