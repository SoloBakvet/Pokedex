from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from app.db.database import SessionLocal

from app.models.pokemon_model import PokemonDBModel, PokemonSpritesDBModel, PokemonTypeDBModel, PokemonAbilityDBModel, PokemonStatDBModel, PokemonMoveDBModel, VersionGroupDetailsDBModel
from app.schemas.pokemon.pokemon_schema import SimplePokemon, Pokemon

def query_pokemons(sort: str , db: Session) -> List[SimplePokemon]:
    simple_pokemons = list()
    db_pokemons = db.query(PokemonDBModel).all()
    for db_pokemon in db_pokemons:
        simple_pokemons.append(SimplePokemon.model_validate(db_pokemon))
    return simple_pokemons
def query_pokemon(pokemon_id: int , db: Session) -> Pokemon:
    db_pokemon= db.query(PokemonDBModel).filter_by(id=pokemon_id).first()
    if(db_pokemon is None):
        raise NoResultFound
    return Pokemon.model_validate(db_pokemon)

def create_pokemon(pokemon: Pokemon, db: Session) -> Pokemon:
    pokemon_json = pokemon.model_dump()
    # Remove nested pydantic models because they lead to parsing errors
    del pokemon_json['types']
    del pokemon_json['sprites']
    del pokemon_json['stats']
    del pokemon_json['abilities']
    del pokemon_json['moves']
    
    db_pokemon = PokemonDBModel(**pokemon_json)
    db_pokemon_sprites = PokemonSpritesDBModel(**pokemon.sprites.model_dump(), pokemon_id=db_pokemon.id)

    db_pokemon_types = list()
    for type in pokemon.types:
        db_pokemon_types.append(PokemonTypeDBModel(**type.model_dump(), pokemon_id=db_pokemon.id))
    db_pokemon_abilities = list()
    for ability in pokemon.abilities:
        db_pokemon_abilities.append(PokemonAbilityDBModel(**ability.model_dump(), pokemon_id=db_pokemon.id))
    db_pokemon_stats = list()
    for stat in pokemon.stats:
        db_pokemon_stats.append(PokemonStatDBModel(**stat.model_dump(), pokemon_id=db_pokemon.id))
    db_pokemon_moves = list()
    for move in pokemon.moves:
        move_json = move.model_dump()
        del move_json['version_group_details']
        db_move = PokemonMoveDBModel(**move_json, pokemon_id=db_pokemon.id)
        for version_group_details in move.version_group_details:
            db_move.version_group_details.append(VersionGroupDetailsDBModel(**version_group_details.model_dump()))
        db_pokemon_moves.append(db_move)
        
    db.add(db_pokemon)
    db.add(db_pokemon_sprites)
    db.add_all(db_pokemon_types)
    db.add_all(db_pokemon_abilities)
    db.add_all(db_pokemon_stats)
    db.add_all(db_pokemon_moves)
        

    db.commit()
    return 

# def create_pokemons(pokemons: List[Pokemon], db: Session):
#     for pokemon in pokemons:
#         try:
#             create_pokemon(pokemon=pokemon, db=db)
#         except:
#             pass