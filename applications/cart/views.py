from django.shortcuts import render
from django.views.generic import ListView

from .models import Sale



class AllProductsCart(ListView):
    template_name = 'cart/view_cart.html'
    context_object_name = 'products'
    model = Sale

    def get_context_data(self, **kwargs):
        context =  super(AllProductsCart, self).get_context_data(**kwargs)
        context['sale'] = Sale.objects.all()
        return context




