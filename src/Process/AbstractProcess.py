from abc import ABC, abstractmethod
from typing_extensions import Self

class AbstractProcess(ABC):
    @abstractmethod
    def execute(self: Self):
        pass