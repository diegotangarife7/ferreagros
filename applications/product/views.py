from django.shortcuts import render
from django.views.generic import ListView


from .models import Category, Product


class ListAllCategoriesAndProducts(ListView):
    template_name = 'product/all_categories_products.html'

    def get_queryset(self):
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ListAllCategoriesAndProducts, self). get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['all_products'] = Product.objects.all()
        return context
    

def list_by_category(request, slug):
    categories = Category.objects.all()
    name_category = Category.objects.get(slug=slug)
    products = name_category.product_set.all()
    context = {
        'all_products': products,
        'all_categories': categories
    }
    return render(request, 'product/all_categories_products.html', context)


def detail_product(request):
    return render(request, 'product/detail_product.html')





    
    




    


    




