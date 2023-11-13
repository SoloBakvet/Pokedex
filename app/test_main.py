from fastapi.testclient import TestClient

from app.main import app
from app.schemas.pokemon.pokemon_schema import Pokemon, SimplePokemon

client = TestClient(app)

def test_get_pokemon_with_id():
    response = client.get("/api/v1/pokemons/10")
    pokemon = Pokemon(**response.json())
    assert response.status_code == 200
    assert pokemon.name == "caterpie" 
    assert pokemon.types[0].type == "bug"
    
def test_search_pokemon():
    response = client.get("/api/v1/search/?query=bulbasaur")
    pokemon = SimplePokemon(**(response.json()[0]))
    assert response.status_code == 200
    assert pokemon.name == "bulbasaur" 
    assert pokemon.types[0].type == "grass"
    
