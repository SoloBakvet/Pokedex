from typing import List
from pydantic import BaseModel

class Team(BaseModel):
    id : int
    name : str
    pokemons : List[int]
    type : str
    
    class Config:
        from_attributes = True