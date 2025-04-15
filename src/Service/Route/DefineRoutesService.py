from typing_extensions import Self

from fastapi import APIRouter

from src.Process.Route import DefineUserRoutesProcess, DefineDiscussionRoutesProcess, DefineProjectRoutesProcess


class DefineRoutesService():
    def __init__(self: Self):
        self.define_project_routes_process: DefineProjectRoutesProcess = DefineProjectRoutesProcess()
        self.define_user_routes_process: DefineUserRoutesProcess = DefineUserRoutesProcess()
        self.define_discussion_routes_process: DefineDiscussionRoutesProcess = DefineDiscussionRoutesProcess()
        self.router: APIRouter = APIRouter()

    def add_user_routes(self: Self) -> Self:
        self.get_router().include_router(self.get_define_user_routes_process().execute())
        return self

    def add_project_routes(self: Self) -> Self:
        self.get_router().include_router(self.get_define_project_routes_process().execute())
        return self

    def add_discussion_routes(self: Self) -> Self:
        self.get_router().include_router(self.get_define_discussion_routes_process().execute())
        return self

    def get_define_user_routes_process(self: Self) -> DefineUserRoutesProcess:
        return self.define_user_routes_process

    def get_define_project_routes_process(self: Self) -> DefineProjectRoutesProcess:
        return self.define_project_routes_process

    def get_define_discussion_routes_process(self: Self) -> DefineDiscussionRoutesProcess:
        return self.define_discussion_routes_process

    def get_router(self: Self) -> APIRouter:
        return self.router