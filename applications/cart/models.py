from django.db import models
from django.conf import settings

from applications.product.models import Product


class Sale(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='producto')
    quantity = models.PositiveIntegerField('cantidad')
    total = models.DecimalField('total',max_digits=10, decimal_places=2)

    def calculate_total(self):
        if self.product.discounted_price > 0:
            self.product.price = self.product.discounted_price
        return float(self.product.price * self.quantity)
    
    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
    
    class Meta:
        db_table = 'Venta'
        verbose_name ='venta'
        verbose_name_plural = 'ventas'
    