from pydantic import BaseModel

class Stat(BaseModel):
    name: str
    url: str
    
class PokemonStat(BaseModel):
    base_stat: int
    effort: int
    stat: Stat
    