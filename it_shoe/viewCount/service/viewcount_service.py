from abc import ABC, abstractmethod

class ViewCountService(ABC):

    @abstractmethod
    def increment_community_view_count(self, communityId):
        pass
    @abstractmethod
    def increment_review_view_count(self, reviewId):
        pass
