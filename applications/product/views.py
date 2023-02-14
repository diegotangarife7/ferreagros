from django.shortcuts import render

# Create your views here.



def all_product(request):
    return render(request, 'product/all_products.html')