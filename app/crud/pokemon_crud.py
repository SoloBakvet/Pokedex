from typing import List
from sqlalchemy.orm import Session

from app.models.pokemon_model import PokemonDBModel, PokemonDetailsDBModel,SimpleSpriteDBModel, PokemonTypeDBModel, AdvancedSpriteDBModel
from app.schemas.pokemon.pokemon_schema import SimplePokemon, Pokemon

def query_pokemons(sort: str , db: Session) -> List[Pokemon]:
    return Pokemon.model_validate(db.query(PokemonDBModel).all())

def query_pokemon(id: int , db: Session) -> Pokemon:
    return db.query(PokemonDBModel).all()

# def create_pokemon(pokemon: Pokemon, db: Session) -> Pokemon:
#     db_pokemon = PokemonDBModel(id=pokemon.id, name=pokemon.name)
#     db_simple_sprite = SimpleSpriteDBModel(front_default=pokemon.sprites.front_default, pokemon_id=pokemon.id)
#     db_pokemon_types = list()
#     for pokemon_type in pokemon.types:
#         db_pokemon_types.append(PokemonTypeDBModel(slot=pokemon_type.slot, pokemon_id=pokemon.id, type=pokemon_type.type))
#     db.add_all(db_pokemon_types)
#     db.add(db_pokemon)
#     db.add(db_simple_sprite)
    
#     db_pokemon_details = PokemonDetailsDBModel(id=pokemon_details.id, pokemon_id=pokemon.id, height=pokemon_details.height,
#                                                weight=pokemon_details.weight,
#                                                order=pokemon_details.order,
#                                                species=pokemon_details.species)
#     db_advanced_sprite = AdvancedSpriteDBModel( details_id=pokemon_details.id, front_default=pokemon_details.sprites.front_default,
#                                                front_female=pokemon_details.sprites.front_female,
#                                                front_shiny=pokemon_details.sprites.front_shiny,
#                                                front_shiny_female=pokemon_details.sprites.front_shiny_female,
#                                                back_default=pokemon_details.sprites.back_default,
#                                                back_female=pokemon_details.sprites.back_female,
#                                                back_shiny=pokemon_details.sprites.back_shiny,
#                                                back_shiny_female=pokemon_details.sprites.back_shiny_female)
#     db.add(db_pokemon_details)
#     db.add(db_advanced_sprite)
#     db.commit()
#     return db.query(PokemonDBModel).filter(id=pokemon.id).first()

# def create_pokemons(pokemons: List[Pokemon], db: Session):
#     for pokemon in pokemons:
#         try:
#             create_pokemon(pokemon=pokemon, db=db)
#         except:
#             pass