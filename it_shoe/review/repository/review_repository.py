from abc import ABC, abstractmethod


class ReviewRepository(ABC):
    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def create(self, title, writer, content, rating, reviewImage):
        pass

    @abstractmethod
    def findByReviewId(self, reviewId):
        pass