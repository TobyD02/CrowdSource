from abc import abstractmethod
from typing_extensions import Self

from src.Process import AbstractProcess

from fastapi import APIRouter

class AbstractDefineRoutesProcess(AbstractProcess):

    @abstractmethod
    def execute(self: Self) -> APIRouter:
        pass