from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, TemplateView

from .models import Sale
from applications.users.models import User
from applications.product.models import Product
from .cart import ShoppingCart



class AllProductsCart(TemplateView):
    template_name = 'cart/view_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart', {})

        total_sale = 0
        items = []

        for key, value in cart.items():
            product = value['product']
            quantity = value['quantity']
            total = value['total']
            total_sale += value['total']

            item = {
                'key': key,
                'product': product,
                'quantity': quantity,
                'total': total
            }    
            items.append(item)

        total_of_prducts = 0
        for item in items:
            total_of_prducts += item['quantity']

        context['items'] = items
        context['total_sale'] = total_sale
        context['total_of_prducts'] = total_of_prducts

        return context


def add_product_cart(request, id):
    product = Product.objects.get(id=id)
    cart = ShoppingCart(request)
    cart.add(product.id)
    current_url =  request.META.get('HTTP_REFERER')
    return redirect(current_url)

    
def delete_product_cart(request, id):
    product = Product.objects.get(id=id)
    cart = ShoppingCart(request)
    cart.delete(product.id)
    return redirect('cart_app:cart_sale')


def subtract_product_cart(request, id):
    product = Product.objects.get(id=id)
    cart = ShoppingCart(request)
    cart.subtract(product.id)
    return redirect('cart_app:cart_sale')

    
    



    
        
        


