from pydantic import BaseModel, Field
from typing import List, Optional

class Type(BaseModel):
    name : str

class PokemonType(BaseModel):
    slot : int = Field(ge=0)
    type : Type

class SimpleSprite(BaseModel):
    front_default : str
    
class AdvancedSprite(BaseModel):
    front_default : str
    front_female : Optional[str] = None
    front_shiny : str
    front_shiny_female : Optional[str] = None
    back_default : str
    back_female : Optional[str] = None
    back_shiny : str
    back_shiny_female : Optional[str] = None
    
# TODO: Implement
class PokemonMove(BaseModel):
    pass

class Pokemon(BaseModel):
    id : int
    name : str
    sprites : SimpleSprite
    types : List[PokemonType]
    
# TODO: Add missing fields
class PokemonDetails(BaseModel):
    id : int
    name : str
    sprites : AdvancedSprite
    types : List[PokemonType]
    #moves : List[PokemonMove]
    height : int
    weight : int
    order : int
    #species : str
    #form : str