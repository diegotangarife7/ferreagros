from django.shortcuts import render
from django.views.generic import ListView, DetailView


from .models import Category, Product, ProductImages


class ListAllCategoriesAndProducts(ListView):
    template_name = 'product/all_categories_products.html'

    def get_queryset(self):
        return Category.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(ListAllCategoriesAndProducts, self). get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        context['all_products'] = Product.objects.all().order_by('-created')
        return context
    

def list_by_category(request, slug):
    categories = Category.objects.all()
    name_category = Category.objects.get(slug=slug)
    products = name_category.product_set.all().order_by('-created')
    context = {
        'all_products': products,
        'all_categories': categories
    }
    return render(request, 'product/all_categories_products.html', context)


class DetailProduct(DetailView):
    model = Product
    template_name = 'product/detail_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        product_url = self.kwargs['slug']
        product = Product.objects.get(slug=product_url)

        images_product = ProductImages.objects.filter(product=product)
        images_product = images_product[:3]
        
        product_categories = Product.objects.get(id=product.id)
        categories = product_categories.categories.all()
        categories = categories[:3]

        context['product'] = product
        context['list_images'] = images_product
        context['categories'] = categories

        return context




    
    




    


    




