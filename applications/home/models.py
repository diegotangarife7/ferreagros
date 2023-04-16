from django.db import models
from django.conf import settings



class AboutUs(models.Model):                     
    created =               models.DateTimeField(auto_now_add=True) 
    user =                  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title =                 models.CharField(max_length=60, verbose_name='Primer titulo')
    description =           models.TextField(verbose_name='descripcion del primer titulo')
    principal_image =       models.ImageField(upload_to='about_as/principal_image/%Y/%m/%d/', verbose_name='imagen principal')
    title_1 =               models.CharField(default='Quines somos', max_length=30, verbose_name='titulo 1')
    description_title_1 =   models.TextField(verbose_name='descripcion titulo 1')
    avatar =                models.ImageField(upload_to='about_as/avatar/%Y/%m/%d/', verbose_name='foto')
    name_avatar =           models.CharField(max_length=50, verbose_name='Nombre')
    description_avatar =    models.CharField(max_length=300)
    title_2 =               models.CharField(max_length=30, default='Visión', verbose_name='titulo 2')
    description_title_2 =   models.TextField(verbose_name='descripcion titulo 2')
    title_3 =               models.CharField(max_length=30, default='Fundación', verbose_name='titulo 3')
    description_title_3 =   models.TextField(verbose_name='descripcion titulo 3')


    def __str__(self):
        return str(self.id) + ') ' + self.title_1 + ' --- ' +  str(self.created)
    
    class Meta:
        db_table = 'sobre nosotros'
        verbose_name_plural = 'sobre nosotros'
