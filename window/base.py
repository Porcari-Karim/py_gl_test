from abc import ABC, abstractmethod

class BaseWindow(ABC):

    @abstractmethod
    def __init__(self, width:int, height:int, title:int):
        pass

    @abstractmethod
    def present(self):
        pass

    @abstractmethod
    def poll_events(self):
        pass

    @abstractmethod
    def should_close(self):
        pass

    @abstractmethod
    def use_context(self):
        pass
