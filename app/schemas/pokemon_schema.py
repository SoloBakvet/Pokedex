from typing import List, Optional
from pydantic import BaseModel, Field
     
class PokemonType(BaseModel):
    slot : int = Field(ge=1)
    type : str
    
    class Config:
        from_attributes = True
        
class PokemonMove(BaseModel):
    move : str
    #version_group_details: List[]
        
class SimpleSprite(BaseModel):
    front_default : str
    
    class Config:
        from_attributes = True
        
class AdvancedSprite(BaseModel):
    front_default : str
    front_female : Optional[str] = None
    front_shiny : str
    front_shiny_female : Optional[str] = None
    back_default : str
    back_female : Optional[str] = None
    back_shiny : str
    back_shiny_female : Optional[str] = None
        
class Pokemon(BaseModel):
    id: int = Field(ge=1)
    name : str
    sprites : SimpleSprite
    types : List[PokemonType]

    class Config:
        from_attributes = True
        
# TODO: Implement extra fields
class PokemonDetails(BaseModel):
    id : int
    name : str
    sprites : AdvancedSprite
    types : List[PokemonType]
    height : int
    weight : int
    moves : List[PokemonMove]
    order : int
    #species : str
    #form : str
        

        
