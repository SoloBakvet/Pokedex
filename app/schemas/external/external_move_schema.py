from typing import List
from pydantic import BaseModel

class MoveDetails(BaseModel):
    name: str
    url : str
    
class MoveLearnMethod(BaseModel):
    name: str
    url : str
    
class VersionGroupDetails(BaseModel):
    name: str
    url : str
    
class VersionGroup(BaseModel):
    level_learned_at: int
    move_learn_method: MoveLearnMethod
    version_group: VersionGroupDetails
    
class Move(BaseModel):
    move: MoveDetails
    version_group_details: List[VersionGroup]
    