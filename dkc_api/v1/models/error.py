from pydantic import BaseModel

class ResponceError(BaseModel):
    code: int
    message: str
    
class ResponceErrorAlternative(BaseModel):
    errorCode: str
    errorMessage: str