from typing_extensions import Self
from typing import List

from fastapi import APIRouter

from src.Service.Route import DefineRoutesService

class Routes:
    def __init__(self: Self):
        self.router: APIRouter = APIRouter()
        self.define_routes_service: DefineRoutesService = DefineRoutesService()

    def get_routes(self: Self) -> APIRouter:
        self.router = self.get_define_routes_service() \
            .add_user_routes() \
            .add_project_routes() \
            .add_discussion_routes() \
            .get_router()

        return self.get_router()

    def get_define_routes_service(self: Self) -> DefineRoutesService:
        return self.define_routes_service

    def get_router(self: Self) -> APIRouter:
        return self.router


