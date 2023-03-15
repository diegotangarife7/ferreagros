from django.urls import path
from . import views


app_name = 'cart_app'

urlpatterns = [
    path('carrito/', views.AllProductsCart.as_view(), name='cart_sale')

    
]
