from product.entity.models import Product
from viewCount.entity.product_viewcount import ProductViewCount
from viewCount.repository.viewcount_product_repository import ViewCountProductRepository


class ViewCountProductRepositoryImpl(ViewCountProductRepository):

    def increment_product_view_count(self, productId):
        try:
            product = Product.objects.get(pk=productId)
            view_count, created = ProductViewCount.objects.get_or_create(product=product)
            view_count.increment()
            return view_count.count
        except Product.DoesNotExist:
            return None