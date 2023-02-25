from django.urls import path

from . import views


app_name='product_app'


urlpatterns = [
    path('todos/categorias/productos/', views.ListAllCategoriesAndProducts.as_view(), name='all_categories_products'),
    path('todos/categorias/productos/<slug:slug>/', views.list_by_category, name='filtered_by_categories'),
    path('producto/detail/<slug:slug>/', views.DetailProduct.as_view(), name='detail_product'),
    path('busqueda/filtros/', views.MultipleFilters.as_view(), name='multiple_filters'),

]
