from typing import List
from typing_extensions import Self

from fastapi import APIRouter

from src.ConfigProvider import ConfigProvider
from src.Controller import ProjectController
from src.Model.Project import CreateProjectRequestModel
from src.Process.Route.AbstractDefineRoutesProcess import AbstractDefineRoutesProcess


class DefineProjectRoutesProcess(AbstractDefineRoutesProcess):
    def __init__(self: Self):
        self.routes: List = []
        self.router: APIRouter = APIRouter()
        self.project_controller: ProjectController = ProjectController()
        self.config_provider: ConfigProvider = ConfigProvider()

    def execute(self: Self) -> APIRouter:
        self.register_find_project_by_project_route() \
            .register_create_project_route()

        return self.get_router()

    def register_find_project_by_project_route(self: Self) -> Self:
        @self.get_router().get(
            self.get_config_provider().get_config()["server"]["BaseRoute"] + "/api/project/{project}"
        )
        async def find_project_by_project(project: str):
            return await self.get_project_controller().find_project(project)

        return self

    def register_create_project_route(self: Self) -> Self:
        @self.get_router().post(
            self.get_config_provider().get_config()["server"]["BaseRoute"] + "/api/project"
        )
        async def find_project_by_project(project: CreateProjectRequestModel):
            return await self.get_project_controller().create_project(project)

        return self

    def get_router(self: Self) -> APIRouter:
        return self.router
    
    def get_project_controller(self) -> ProjectController:
        return self.project_controller

    def get_config_provider(self: Self) -> ConfigProvider:
        return self.config_provider
