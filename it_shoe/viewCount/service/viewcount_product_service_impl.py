from viewCount.repository.viewcount_product_repository_impl import ViewCountProductRepositoryImpl
from viewCount.service.viewcount_product_service import ViewCountProductService


class ViewCountProductServiceImpl(ViewCountProductService):
    def __init__(self):
        self.repository = ViewCountProductRepositoryImpl()

    def increment_product_view_count(self, productId):
        return self.repository.increment_product_view_count(productId)