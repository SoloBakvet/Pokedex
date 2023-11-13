import json
import argparse
import requests

from app.db import database
from app.schemas.external.external_helper import parse_external_into_internal_pokemon
from app.schemas.external.external_pokemon_schema import ExternalPokemon
from app.crud import pokemon_crud

def import_pokemons_from_json(args):
    try:
        db = next(database.get_db())
        with open(args.file) as file:
            loaded_json = json.load(file)
            for pokemon_json in loaded_json:
                try:
                    pokemon = parse_external_into_internal_pokemon(ExternalPokemon(**pokemon_json))
                    pokemon_crud.create_pokemon(pokemon=pokemon, db=db)
                    print("Imported pokemon: " + pokemon.name + " (id=" + str(pokemon.id) + ")")
                except:
                    print("Failed to import a pokemon.")

    except FileNotFoundError:
        print('File not found.')
        
def import_external_pokemon(args):
    try:
        db = next(database.get_db())
        response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(args.id))
        pokemon = parse_external_into_internal_pokemon(ExternalPokemon(**response.json()))
        pokemon_crud.create_pokemon(pokemon=pokemon, db=db)
        print("Imported pokemon: " + pokemon.name + " (id=" + str(pokemon.id) + ")")
    except:
        print("Failed to import a pokemon.")
    
parser = argparse.ArgumentParser(description = "An addon to import pokemons from various sources.")
subparsers = parser.add_subparsers()

json_parser = subparsers.add_parser('json', help="Import pokemons from JSON file.")
json_parser.add_argument('file', type=str, help="JSON file to import from.")
json_parser.set_defaults(func=import_pokemons_from_json)

external_parser = subparsers.add_parser('external', help="Import pokemon from external API.")
external_parser.add_argument('id', type=int, help="Id of of pokemon to import.")
external_parser.set_defaults(func=import_external_pokemon)

database.Base.metadata.create_all(bind=database.engine)

args = parser.parse_args()
args.func(args)
 
