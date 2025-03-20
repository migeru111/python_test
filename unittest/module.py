from abc import ABC,abstractmethod
from unittest.mock import Mock

class BaseUsecase(ABC):
    @abstractmethod
    def execute(self):
        pass

class Usecase1(BaseUsecase):

    def execute(self):
        return "usecase1"

class Controller:
    def __init__(self,**kwargs):
        self.__usecase1=kwargs.get("usecase1",Mock())
        self.__usecase2=kwargs.get("usecase2",Mock())
        print(self.__usecase1,self.__usecase2)

    def route_usecase1(self):
        return self.__usecase1.execute()