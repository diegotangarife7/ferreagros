from django.urls import path
from . import views


app_name = 'cart_app'

urlpatterns = [
    # Cart
    path('carrito/', views.AllProductsCart.as_view(), name='cart_sale'),
    path('add-product/<int:id>/', views.add_product_cart, name='add_product'),
    path('delete-product/<int:id>/', views.delete_product_cart, name='delete_product'),
    path('subtract-product/<int:id>/', views.subtract_product_cart, name='subtract_product'),
    # Favorites
    path('add-product-favorite/<int:id>/', views.add_product_favorite, name='add_product_favorite'),
    path('productos/favoritos/', views.ListProductFavorites.as_view(), name='products_favorite_by_user'),

]
