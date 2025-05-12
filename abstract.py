#  a class that can not be subsatntiated
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass  