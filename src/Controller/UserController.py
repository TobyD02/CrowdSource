from typing_extensions import Self

from src.Model.User import CreateUserRequestModel


class UserController:
    def __init__(self: Self):
        self.user_by_username_service = None

    async def find_user_by_username(self: Self, username: str):
        return {"route": "find_user_by_username", "username": username}

    async def create_user(self: Self, user: CreateUserRequestModel):
        return {"route": "create_user", "username": user.username, "password": user.password}
