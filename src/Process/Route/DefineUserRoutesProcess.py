from typing import List
from typing_extensions import Self

from fastapi import APIRouter

from src.ConfigProvider import ConfigProvider
from src.Controller import UserController
from src.Model.User import CreateUserRequestModel
from src.Process.Route.AbstractDefineRoutesProcess import AbstractDefineRoutesProcess


class DefineUserRoutesProcess(AbstractDefineRoutesProcess):
    def __init__(self: Self):
        self.routes: List = []
        self.router: APIRouter = APIRouter()
        self.user_controller: UserController = UserController()
        self.config_provider: ConfigProvider = ConfigProvider()

    def register_routes(self: Self) -> Self:
        return self \
            .register_create_user_route() \
            .register_find_user_by_username_route()

    def register_find_user_by_username_route(self: Self) -> Self:
        @self.get_router().get(
            self.get_config_provider().get_config()["server"]["BaseRoute"] + "/api/user/{username}"
        )
        async def find_user_by_username(username: str):
            return await self.get_user_controller().find_user_by_username(username)

        return self

    def register_create_user_route(self: Self) -> Self:
        @self.get_router().post(
            self.get_config_provider().get_config()["server"]["BaseRoute"] + "/api/user"
        )
        async def find_user_by_username(user: CreateUserRequestModel):
            return await self.get_user_controller().create_user(user)

        return self

    def get_router(self: Self) -> APIRouter:
        return self.router
    
    def get_user_controller(self) -> UserController:
        return self.user_controller

    def get_config_provider(self: Self) -> ConfigProvider:
        return self.config_provider
