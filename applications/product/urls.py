from django.urls import path

from . import views


app_name='product_app'


urlpatterns = [
    path('productos/todos', views.all_product, name="all_products")
]
