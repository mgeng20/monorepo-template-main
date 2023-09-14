from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def set_values(self):
        pass

    @abstractmethod
    def area(self):
        pass
