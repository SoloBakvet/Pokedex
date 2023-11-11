from typing import Optional
from pydantic import BaseModel

class Sprite(BaseModel):
    front_default: str
    front_femal : Optional[str] = None
    front_shiny: str
    front_shiny_female: Optional[str] = None
    back_default: str
    back_female: Optional[str] = None
    back_shiny: str
    back_shiny_female: Optional[str] = None
    