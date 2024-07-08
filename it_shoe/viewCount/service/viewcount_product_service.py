from abc import ABC, abstractmethod

class ViewCountProductService(ABC):

    @abstractmethod
    def increment_product_view_count(self, productId):
        pass