from abc import ABC, abstractmethod

class ViewCountRepository(ABC):

    @abstractmethod
    def increment_view_count(self, communityId):
        pass
