from cart.entity.cart import Cart
from cart.entity.cart_item import CartItem
from cart.repository.cart_item_repository import CartItemRepository


class CartItemRepositoryImpl(CartItemRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def register(self, cartData, cart, product):
        productPrice = cartData.get('productPrice')
        quantity = cartData.get('quantity')
        productSize = cartData.get('productSize')  # productSize 추가

        CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=quantity,
            price=productPrice,
            productSize = productSize
        )

    def findById(self, id):
        return CartItem.objects.get(cartItemId=id)

    def findByCart(self, cart):
        return list(CartItem.objects.filter(cart=cart))

    def findByProductId(self, productId):
        try:
            return CartItem.objects.get(product_id=productId)
        except CartItem.DoesNotExist:
            return None

    def findAllByProductIdAndProductSize(self, productId, productSize):
        return CartItem.objects.filter(product_id=productId, productSize=productSize)

    def deleteByCartItemId(self, cartItem_Id):
        for cartItemId in cartItem_Id:
            cartItem = CartItem.objects.get(cartItemId=cartItemId)
            cartItem.delete()

    def update(self, cartItem):
        cartItem.save()
