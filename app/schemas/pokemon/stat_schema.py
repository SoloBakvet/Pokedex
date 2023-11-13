from pydantic import BaseModel

class PokemonStat(BaseModel):
    stat: str
    base_stat: int
    effort: int
    
    class Config:
        from_attributes = True
        