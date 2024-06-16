from abc import ABC, abstractmethod

class OauthService(ABC):

    @abstractmethod
    def method(self):
        pass