from abc import ABC, abstractmethod


class BaseMethod(ABC):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError
