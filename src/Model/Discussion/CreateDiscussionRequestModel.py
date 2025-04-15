from pydantic import BaseModel

class CreateDiscussionRequestModel(BaseModel):
    discussion_name: str
    project_id: str