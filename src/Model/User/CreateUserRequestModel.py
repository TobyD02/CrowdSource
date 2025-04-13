from pydantic import BaseModel

class CreateUserRequestModel(BaseModel):
    username: str
    password: str