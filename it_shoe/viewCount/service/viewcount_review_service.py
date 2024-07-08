from abc import ABC, abstractmethod

class ViewCountReviewService(ABC):

    @abstractmethod
    def increment_review_view_count(self, reviewId):
        pass