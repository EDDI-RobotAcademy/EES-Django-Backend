from django.db import models

from account.entity.account import Account

from orders.entity.orders_status import OrderStatus


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    size = models.PositiveIntegerField(default=220)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=10, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    created_date = models.DateTimeField(auto_now=True)
    
    def total_price(self):
        from orders.entity.orders_item import OrdersItem
        order_items =  OrdersItem.objects.filter(orders=self)
        total_price = sum([order_item.total_price() for order_item in order_items])
        return total_price
    
    def total_quantity(self):
        from orders.entity.orders_item import OrdersItem
        order_items =  OrdersItem.objects.filter(orders=self)
        total_quantity = sum([order_item.quantity for order_item in order_items])
        return total_quantity

    def save(self, *args, **kwargs):
        if 'force_created_date' in kwargs:
            self._meta.get_field('created_date').auto_now = False
            self.created_date = kwargs.pop('force_created_date')
        super().save(*args, **kwargs)
        if 'force_created_date' not in kwargs:
            self._meta.get_field('created_date').auto_now = True

    def __str__(self):
        return f"Orders {self.id} by {self.account}"

    class Meta:
        db_table = 'orders'
        app_label = 'orders'
