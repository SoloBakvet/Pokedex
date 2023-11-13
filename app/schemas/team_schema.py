from typing import List
from pydantic import BaseModel

class CreateTeamRequest(BaseModel):
    name : str

class Team(BaseModel):
    id : int
    name : str
    pokemons : List[int] = []
    
    class Config:
        from_attributes = True
        