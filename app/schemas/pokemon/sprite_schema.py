from typing import Optional

from pydantic import BaseModel


class SimplePokemonSprite(BaseModel):
    front_default : str
    
    class Config:
        from_attributes = True
        
class PokemonSprite(BaseModel):
    front_default : str
    front_female : Optional[str] = None
    front_shiny : str
    front_shiny_female : Optional[str] = None
    back_default : str
    back_female : Optional[str] = None
    back_shiny : str
    back_shiny_female : Optional[str] = None
    
    class Config:
        from_attributes = True