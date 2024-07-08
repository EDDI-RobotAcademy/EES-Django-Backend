from abc import ABC, abstractmethod

class ViewCountProductRepository(ABC):

    @abstractmethod
    def increment_product_view_count(self, productId):
        pass