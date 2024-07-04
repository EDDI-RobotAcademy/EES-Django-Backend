from abc import ABC, abstractmethod

class ViewCountService(ABC):

    @abstractmethod
    def increment_view_count(self, communityId):
        pass
