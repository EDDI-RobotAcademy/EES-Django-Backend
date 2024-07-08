from abc import ABC, abstractmethod

class ViewCountReviewRepository(ABC):

    @abstractmethod
    def increment_review_view_count(self, reviewId):
        pass