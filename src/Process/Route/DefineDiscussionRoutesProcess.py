from typing import List
from typing_extensions import Self

from fastapi import APIRouter

from src.ConfigProvider import ConfigProvider
from src.Controller import DiscussionController
from src.Model.Discussion import CreateDiscussionRequestModel
from src.Process.Route.AbstractDefineRoutesProcess import AbstractDefineRoutesProcess


class DefineDiscussionRoutesProcess(AbstractDefineRoutesProcess):
    def __init__(self: Self):
        self.routes: List = []
        self.router: APIRouter = APIRouter()
        self.discussion_controller: DiscussionController = DiscussionController()
        self.config_provider: ConfigProvider = ConfigProvider()

    def execute(self: Self) -> APIRouter:
        self.register_create_discussion_route() \
            .register_find_discussion_route()

        return self.get_router()

    def register_find_discussion_route(self: Self) -> Self:
        @self.get_router().get(
            self.get_config_provider().get_config()["server"]["BaseRoute"] + "/api/discussion/{discussion}"
        )
        async def find_discussion(discussion: str):
            return await self.get_discussion_controller().find_discussion(discussion)

        return self

    def register_create_discussion_route(self: Self) -> Self:
        @self.get_router().post(
            self.get_config_provider().get_config()["server"]["BaseRoute"] + "/api/discussion"
        )
        async def find_discussion(discussion: CreateDiscussionRequestModel):
            return await self.get_discussion_controller().create_discussion(discussion)

        return self

    def get_router(self: Self) -> APIRouter:
        return self.router

    def get_discussion_controller(self) -> DiscussionController:
        return self.discussion_controller

    def get_config_provider(self: Self) -> ConfigProvider:
        return self.config_provider
