from applications.product.models import Product
from .models import Sale



class ShoppingCart:

    def __init__(self, request):
        if 'cart' not in request.session:
            request.session['cart'] = {}
        self.request = request

        if not self.request.user.is_authenticated:
            self.request.user = None
            
    def add(self, id):
        id_product = str(id)
        product = Product.objects.get(id=id)
        cart = self.request.session['cart']
        
        if id_product in cart:
            cart[id_product]['product'] = product.name
            cart[id_product]['quantity'] += 1
            sale = Sale(user=self.request.user, product=product, quantity=cart[id_product]['quantity'])
            cart[id_product]['total'] = sale.calculate_total() 
        else:
            cart[id_product] = {'product': product.name, 'quantity': 1}
            sale = Sale(user=self.request.user, product=product, quantity=cart[id_product]['quantity'])
            cart[id_product]['total'] = sale.calculate_total()
        self.request.session['cart'] = cart

    def delete(self, id):
        id_product = str(id)
        cart = self.request.session['cart']
        
        if id_product in cart:
            del cart[id_product]
            self.request.session['cart'] = cart

    def subtract(self, id):
        id_product = str(id)
        product = Product.objects.get(id=id)
        cart = self.request.session['cart']

        if id_product in cart:
            cart[id_product]['quantity'] -= 1
            cart[id_product]['product'] = product.name
            sale = Sale(user=self.request.user, product=product, quantity=cart[id_product]['quantity'])
            cart[id_product]['total'] = sale.calculate_total() 
            if cart[id_product]['quantity'] < 1:
                ShoppingCart.delete(self, id_product)
            self.request.session['cart'] = cart
