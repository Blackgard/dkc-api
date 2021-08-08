from pydantic import BaseModel

class AuthResponceSuccess(BaseModel):
    code: int
    access_token: str
    
class AuthResponceError(BaseModel):
    code: int
    message: str