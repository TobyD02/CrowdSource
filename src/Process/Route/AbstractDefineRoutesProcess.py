from abc import ABC, abstractmethod
from typing_extensions import Self

from fastapi import APIRouter

class AbstractDefineRoutesProcess(ABC):

    @abstractmethod
    def register_routes(self: Self) -> Self:
        pass

    @abstractmethod
    def get_router(self: Self) -> APIRouter:
        pass