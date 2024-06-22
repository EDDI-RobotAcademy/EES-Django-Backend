from abc import ABC, abstractmethod


class ReviewService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createReview(self, reviewData):
        pass