from typing_extensions import Self

from fastapi import APIRouter

from src.Process.Route import DefineUserRoutesProcess
from src.Process.Route import DefineProjectRoutesProcess
from src.Service.AbstractService import AbstractService


class DefineUserRoutesService(AbstractService):
    def __init__(self: Self):
        self.define_project_routes_process: DefineProjectRoutesProcess = DefineProjectRoutesProcess()
        self.define_user_routes_process: DefineUserRoutesProcess = DefineUserRoutesProcess()
        self.router: APIRouter = APIRouter()

    def execute(self: Self) -> APIRouter:
        self.get_router().include_router(self.get_define_user_routes_process().register_routes().get_router())
        self.get_router().include_router(self.get_define_project_routes_process().register_routes().get_router())
        return self.get_router()

    def get_define_user_routes_process(self: Self) -> DefineUserRoutesProcess:
        return self.define_user_routes_process

    def get_define_project_routes_process(self: Self) -> DefineProjectRoutesProcess:
        return self.define_project_routes_process

    def get_router(self: Self) -> APIRouter:
        return self.router