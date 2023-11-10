from pydantic import BaseModel, Field

class Error(BaseModel):
    error : str
    error_message: str