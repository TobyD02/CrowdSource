from pydantic import BaseModel

class CreateProjectRequestModel(BaseModel):
    project_name: str