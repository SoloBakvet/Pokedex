from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.models.pokemon_model import PokemonDBModel, PokemonSpritesDBModel, PokemonTypeDBModel, PokemonAbilityDBModel, PokemonStatDBModel, PokemonMoveDBModel, VersionGroupDetailsDBModel
from app.schemas.pokemon.pokemon_schema import SimplePokemon, Pokemon

def query_pokemons(sort: str | None, limit: int | None, db: Session) -> List[SimplePokemon]:
    if not sort:
        sort = "id-asc"
    sorting_options = {"name-asc": PokemonDBModel.name.asc(),
                       "name-desc": PokemonDBModel.name.desc(),
                       "id-asc": PokemonDBModel.id.asc(),
                       "id-desc": PokemonDBModel.id.desc()}
    simple_pokemons = list()
    db_pokemons = db.query(PokemonDBModel).order_by(sorting_options[sort]).limit(limit).all()
    for db_pokemon in db_pokemons:
        simple_pokemons.append(SimplePokemon.model_validate(db_pokemon))
    return simple_pokemons

def query_pokemon(pokemon_id: int, db: Session) -> Pokemon:
    db_pokemon= db.query(PokemonDBModel).filter_by(id=pokemon_id).first()
    if(db_pokemon is None):
        raise NoResultFound
    return Pokemon.model_validate(db_pokemon)

def advanced_pokemon_query(query : str, limit: int | None, db: Session) -> List[SimplePokemon]:
    simple_pokemons = list()
    db_pokemons = db.query(PokemonDBModel).filter_by(name=query).limit(limit).all()
    if(len(db_pokemons) == 0):
        db_pokemons = db.query(PokemonDBModel).filter(PokemonDBModel.types.any(type=query)).limit(limit).all()
    for db_pokemon in db_pokemons:
        simple_pokemons.append(SimplePokemon.model_validate(db_pokemon))
    return simple_pokemons

def create_pokemon(pokemon: Pokemon, db: Session):
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