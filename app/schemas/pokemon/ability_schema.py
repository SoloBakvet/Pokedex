from pydantic import BaseModel

class PokemonAbility(BaseModel):
    ability: str
    is_hidden: bool
    slot: int
    
    class Config:
        from_attributes = True
        