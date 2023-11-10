from sqlalchemy.orm import Session


from app.models.pokemon_model import PokemonDBModel,SimpleSpriteDBModel, PokemonTypeDBModel
from app.schemas.pokemon_schema import Pokemon



def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PokemonDBModel).offset(skip).limit(limit).all()

def create_pokemon(db: Session, pokemon: Pokemon, skip: int = 0, limit: int = 100):
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
    return db.query(PokemonDBModel).offset(skip).limit(limit).all()