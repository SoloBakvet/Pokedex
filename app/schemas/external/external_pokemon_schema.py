from typing import List
from pydantic import BaseModel, Field
from app.schemas.external.external_ability_schema import Ability
from app.schemas.external.external_move_schema import Move
from app.schemas.external.external_sprite_schema import Sprite
from app.schemas.external.external_stat_schema import PokemonStat
from app.schemas.external.external_type_schema import PokemonType

class Species(BaseModel):
    name: str
    
class Form(BaseModel):
    name: str
    
class ExternalPokemon(BaseModel):
    id: int = Field(ge=1)
    name: str
    sprites: Sprite
    types: List[PokemonType]
    height: int
    weight: int
    moves: List[Move]
    order: int
    species: Species
    stats: List[PokemonStat]
    abilities: List[Ability]
    forms: List[Form]
