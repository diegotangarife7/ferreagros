from django.db import models


from applications.product.models import Product


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='producto')
    quantity = models.PositiveIntegerField('cantidad')

    def __str__(self):
        return self.product.name
    
    class Meta:
        db_table = 'Venta'
        verbose_name='venta'
        verbose_name_plural = 'ventas'
    

    