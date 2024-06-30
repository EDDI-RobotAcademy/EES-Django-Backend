from abc import ABC, abstractmethod


class ReviewService(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def createReview(self, title, writer, content, rating, reviewImage):
        pass

    @abstractmethod
    def readReview(self, reviewId):
        pass