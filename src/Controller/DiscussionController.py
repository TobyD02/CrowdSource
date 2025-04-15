from typing_extensions import Self

from src.Model.Discussion import CreateDiscussionRequestModel


class DiscussionController:
    def __init__(self: Self):
        self.discussion_by_discussion_service = None

    async def find_discussion(self: Self, discussion: str):
        return {"route": "find_discussion", "discussion": discussion}

    async def create_discussion(self: Self, discussion: CreateDiscussionRequestModel):
        return {"route": "create_discussion", "discussion": discussion.discussion_name, "project_id": discussion.project_id}
