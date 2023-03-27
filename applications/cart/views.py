from django.shortcuts import redirect
from django.views.generic import ListView, TemplateView, DeleteView
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


from .models import Favorite
from applications.product.models import Product
from .cart import ShoppingCart


# Cart

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

    

    
# Favorites

@login_required(login_url='users_app:user_login')
def add_product_favorite(request, id):
    user = request.user
    product = Product.objects.get(id=id)
    
    try:
        favorite = Favorite.objects.create(
            user = user,
            product = product
        )
        favorite.save()
    except:
        IntegrityError

    current_url =  request.META.get('HTTP_REFERER')
    return redirect(current_url)


class ListProductFavorites(LoginRequiredMixin, ListView):
    login_url = 'users_app:user_login'
    template_name = 'cart/favorites.html'

    def get_queryset(self):
        user = self.request.user
        favorite_by_user = Favorite.objects.filter(
            user=user
        ) 
        return favorite_by_user
    

@login_required(login_url='users_app:user_login')
def delete_producto_favorites(request, id):
    
    Favorite.objects.filter(
        id=id
    ).delete()

    current_url =  request.META.get('HTTP_REFERER')
    return redirect(current_url)

    


    
        
        


