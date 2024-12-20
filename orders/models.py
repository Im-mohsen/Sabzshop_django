from django.db import models
from shop.models import Product
from account.models import ShopUser

# Create your models here.


class Order(models.Model):
    buyer = models.ForeignKey(ShopUser, on_delete=models.SET_NULL, related_name='orders', verbose_name='خریدار', null=True)
    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    address = models.CharField(max_length=250, verbose_name='آدرس')
    postal_code = models.CharField(max_length=10, verbose_name='کدپستی')
    province = models.CharField(max_length=50, verbose_name='استان')
    city = models.CharField(max_length=50, verbose_name='شهر')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'

    def __str__(self):
        return f"order {self.id}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_post_cost(self):
        weight = sum(item.get_weight() for item in self.items.all())
        if weight < 1000:
            return 20000
        elif 1000 < weight < 2000:
            return 30000
        else:
            return 50000

    def get_final_cost(self):
        return self.get_total_cost() + self.get_post_cost()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=1)
    weight = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity

    def get_weight(self):
        return self.weight * self.quantity
