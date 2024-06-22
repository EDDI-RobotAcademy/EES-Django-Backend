from abc import ABC, abstractmethod


class ReviewRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, reviewData):
        pass