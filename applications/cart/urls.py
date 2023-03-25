from django.urls import path
from . import views


app_name = 'cart_app'

urlpatterns = [
    path('carrito/', views.AllProductsCart.as_view(), name='cart_sale'),
    path('add-product/<int:id>/', views.add_product_cart, name='add_product'),
    path('delete-product/<int:id>/', views.delete_product_cart, name='delete_product'),
    path('subtract-product/<int:id>/', views.subtract_product_cart, name='subtract_product')
]

