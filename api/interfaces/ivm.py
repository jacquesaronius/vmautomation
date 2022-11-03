from abc import ABC, abstractmethod


class IVM(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.name: str
        self.status: str

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def restart(self):
        pass

    @abstractmethod
    def start(self):
       pass

    @abstractmethod
    def stop(self):
        pass