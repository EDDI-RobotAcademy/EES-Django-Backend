from abc import ABC, abstractmethod

class ViewCountRepository(ABC):

    @abstractmethod
    def increment_community_view_count(self, communityId):
        pass
