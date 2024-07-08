from django.db import models

from cart.entity.cart import Cart
from product.entity.models import Product


class CartItem(models.Model):
    cartItemId = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    productSize = models.PositiveIntegerField(default=0)

    def __str__(self):
        return (f"CartItem -> id: {self.cartItemId}, "
                f"cart: {self.cart.cartId}, "
                f"product: {self.product.productName}, "
                f"quantity: {self.quantity}, "
                f"size: {self.productSize}")  # 필드 표시 추가

    class Meta:
        db_table = 'cart_item'
        app_label = 'cart'

    def getCart(self):
        return self.cart
