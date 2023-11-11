from typing import List

from pydantic import BaseModel, Field

from app.schemas.pokemon.ability_schema import PokemonAbility
from app.schemas.pokemon.move_schema import Move
from app.schemas.pokemon.sprite_schema import SimplePokemonSprite, PokemonSprite
from app.schemas.pokemon.stat_schema import PokemonStat
from app.schemas.pokemon.type_schema import PokemonType
     
           
class SimplePokemon(BaseModel):
    id: int = Field(ge=1)
    name : str
    sprites : SimplePokemonSprite
    types : List[PokemonType]

    class Config:
        from_attributes = True
        
class Pokemon(BaseModel):
    id : int
    name : str
    sprites : PokemonSprite
    types : List[PokemonType]
    height : int
    weight : int
    moves : List[Move]
    order : int
    species : str
    stats: List[PokemonStat]
    abilities: List[PokemonAbility]
    form : str
    
    class Config:
        from_attributes = True
        

        
