from pydantic import BaseModel

class AbilityDetails(BaseModel):
    name: str
    url: str
    
class Ability(BaseModel):
    slot: int
    is_hidden: bool
    ability: AbilityDetails
    