from pydantic import BaseModel, Field


class PokemonType(BaseModel):
    slot : int = Field(ge=1)
    type : str
    
    class Config:
        from_attributes = True
    