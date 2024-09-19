from .mocks import (
    mock_call_endpoint_get_pokemon,
    mock_call_endpoint_all_pokemons
)

def test_get_pokemon_by_id(client, monkeypatch):

    monkeypatch.setattr('src.services.pokemons_service.call_endpoint', 
                        mock_call_endpoint_get_pokemon
    )
    response = client.get("/pokemon/1")
    
    data = response.json
    
    assert response.status_code == 200
    assert 'abilities' in data
    assert 'base_experience' in data
    assert 'cries'in data
    assert 'forms'in data
    assert 'game_indices'in data
    assert 'id'in data
    assert data['id'] == 1
    assert data['name'] == 'bulbasaur'

def test_get_all_pokemons(client, monkeypatch):

    monkeypatch.setattr('src.services.pokemons_service.call_endpoint', 
                        mock_call_endpoint_all_pokemons
    )
    response = client.get("/pokemons")
    
    data = response.json
    
    assert response.status_code == 200
    assert 'count' in data
    assert 'results' in data
    assert 'id' in data['results'][0]
    assert data['results'][0]['id'] == 1
    assert data['results'][0]['name'] == 'bulbasaur'

def test_get_pokemon_by_id_bad_request(client):
   
   response = client.get("/pokemon/bulbasaur")
   data = response.json
   assert response.status_code == 400


def test_get_resource_not_found(client):
   
   response = client.get("/pokemones")
   data = response.json
   assert response.status_code == 404