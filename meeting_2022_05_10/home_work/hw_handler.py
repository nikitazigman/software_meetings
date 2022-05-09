from abc import ABC, abstractmethod


class HandlerInterface(ABC):
    @abstractmethod
    def handle(self, digit: int) -> str:
        pass


class Handler(HandlerInterface):
    def handle(self, digit: int) -> str:
        return "dummy"


def get_handler() -> HandlerInterface:
    """the method returns constructed handler"""
    return Handler()
