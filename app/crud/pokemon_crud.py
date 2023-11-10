from typing import List
from sqlalchemy.orm import Session


from app.models.pokemon_model import PokemonDBModel,SimpleSpriteDBModel, PokemonTypeDBModel
from app.models.team_model import TeamDBModel
from app.schemas.pokemon_schema import PokemonDetails, Pokemon
from app.schemas.team_schema import Team

def query_pokemons(sort: str , db: Session) -> List[Pokemon]:
    return Pokemon.model_validate(db.query(PokemonDBModel).all())

def query_pokemon(id: int , db: Session) -> PokemonDetails:
    return db.query(PokemonDBModel).all()

def create_pokemon(pokemon: Pokemon, db: Session):
    print(pokemon)
    db_pokemon = PokemonDBModel(id=pokemon.id, name=pokemon.name)
    db_sprite = SimpleSpriteDBModel(front_default=pokemon.sprites.front_default, pokemon_id=pokemon.id)
    db_pokemon_types = list()
    for pokemon_type in pokemon.types:
        db_pokemon_types.append(PokemonTypeDBModel(slot=pokemon_type.slot, pokemon_id=pokemon.id, type=pokemon_type.type))
     
    db.add_all(db_pokemon_types)
    db.add(db_pokemon)
    db.add(db_sprite)
    db.commit()
    db.refresh(db_pokemon)
    db.refresh(db_sprite)
    return db.query(PokemonDBModel).all()

def create_pokemons(pokemons: List[Pokemon], db: Session):
    for pokemon in pokemons:
        try:
            create_pokemon(pokemon=pokemon, db=db)
        except:
            pass