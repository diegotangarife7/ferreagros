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