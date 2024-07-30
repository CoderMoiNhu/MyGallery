from typing import TypeVar,List
from abc import ABC,abstractmethod

T=TypeVar('T')

class Interface(ABC):
    @abstractmethod
    def create(self,**kwarg) -> T: pass
    @abstractmethod
    def read(self,**kwarg) -> T: pass
    @abstractmethod
    def update(self,**kwarg) -> T: pass
    @abstractmethod
    def delete(self) -> T: pass
    @abstractmethod
    def count(self, **kwargs) -> T: pass

    @abstractmethod
    def read_all(self, **kwargs) -> List[T]: pass

