import json

from app.schemas.pokemon_schema import PokemonDetails, Pokemon



# TODO: Implement proper database 

pokemon_details_list = list()
pokemon_list = list()

def init_db():
    with open('pokemons.json') as file:
        parsed_json = json.load(file)
        for element in parsed_json:
            pokemon = Pokemon(**element)
            pokemonDetails = PokemonDetails(**element)
            pokemon_list.append(pokemon)
            pokemon_details_list.append(pokemonDetails) 
