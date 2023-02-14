from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=40, verbose_name='nombre')
    description = models.TextField(null=True, blank=True, verbose_name='descripcion')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    image = models.ImageField(upload_to='category', null=True, blank=True, verbose_name='imagen')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categorias'
        verbose_name='categoria'
        verbose_name_plural = 'categorias'


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='nombre')
    description = models.TextField(verbose_name='descripcion')
    price = models.DecimalField(decimal_places=3, max_digits=13, verbose_name='precio')
    principal_image = models.ImageField(upload_to='products', verbose_name='imagen principal')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    categories = models.ManyToManyField(Category, verbose_name='categorias')
    # implementar descuento de precios

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'productos'
        verbose_name='producto'
        verbose_name_plural = 'productos'


class ProductImages(models.Model):
    images = models.ImageField(upload_to='products', verbose_name='imagenes')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images') # con este related_name es como se manejan las imagnes, por ejemplo . Product.images.filter <- example https://youtu.be/_0l_ZalAg6Q?t=753
        

class PrincipalProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='producto de portada')

    class Meta:
        db_table='producto principal'
        verbose_name='producto principal (portada)'
        verbose_name_plural = 'productos principales (portada)'

    

    
