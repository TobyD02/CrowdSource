from typing_extensions import Self
from typing import List

from fastapi import APIRouter

from src.Service import DefineUserRoutesService


class Routes:
    def __init__(self: Self):
        self.router: APIRouter = APIRouter()
        self.define_user_routes_service: DefineUserRoutesService = DefineUserRoutesService()

    def get_routes(self: Self) -> APIRouter:
        self.get_router().include_router(self.get_define_user_routes_service().execute())
        return self.get_router()

    def get_define_user_routes_service(self: Self) -> DefineUserRoutesService:
        return self.define_user_routes_service

    def get_router(self: Self) -> APIRouter:
        return self.router


