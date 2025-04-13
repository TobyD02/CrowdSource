from typing_extensions import Self

from src.Model.Project import CreateProjectRequestModel


class ProjectController:
    def __init__(self: Self):
        self.project_by_project_service = None

    async def find_project(self: Self, project: str):
        return {"route": "find_project", "project": project}

    async def create_project(self: Self, project: CreateProjectRequestModel):
        return {"route": "create_project", "project": project.project_name}
