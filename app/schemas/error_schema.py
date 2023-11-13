from pydantic import BaseModel

class Error(BaseModel):
    error : str
    error_message: str
    