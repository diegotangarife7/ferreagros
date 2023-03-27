from .models import Favorite
from django.contrib.auth.decorators import login_required


def cart_info(request):
    cart = request.session.get('cart', {})
    total_of_products = sum([item['quantity'] for item in cart.values()])

    products_cart = []
    for key, value in cart.items():
        product = value['product']
        quantity = value['quantity']
        item = {'product': product, 'quantity': quantity}
        products_cart.append(item)

    return {
        'total_of_products': total_of_products,
        'products_cart': products_cart,
    }



def favorite_count(request):
    user = request.user
    if user.is_authenticated:
        favorite_by_user = Favorite.objects.filter(user=user)
        favorite_count = Favorite.objects.filter(user=user).count()
        return {
            'favorite_count': favorite_count,
            'favorite_by_user': favorite_by_user
        }
    else:
        return {
            'favorite_count': 0,
        }



