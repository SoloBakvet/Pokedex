from pydantic import BaseModel, Field

class Type(BaseModel):
    name: str
    
class PokemonType(BaseModel):
    slot: int = Field(ge=1)
    type: Type
          