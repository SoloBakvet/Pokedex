from typing import List

from pydantic import BaseModel


class VersionGroupDetails(BaseModel):
    move_learn_method: str
    version_group: str
    level_learned_at: int
    
    class Config:
        from_attributes = True
 
class Move(BaseModel):
    move : str
    version_group_details: List[VersionGroupDetails]
    
    class Config:
        from_attributes = True
    