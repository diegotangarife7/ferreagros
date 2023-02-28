from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Category, Product, ProductImages


class ListAllCategoriesAndProducts(ListView):
    template_name = 'product/all_categories_products.html'
    paginate_by = 6
    context_object_name = 'all_products'
    
    def get_queryset(self):
        return Product.objects.all().order_by('-created')
         
    def get_context_data(self, **kwargs):
        context = super(ListAllCategoriesAndProducts, self). get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        return context
    

def list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    name_category = Category.objects.get(slug=slug)
    products = name_category.product_set.all().order_by('-created')
    context = {
        'selected_category':category,
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


def multiple_filters(request):
    price_min = request.GET.get('price_min',)
    price_max = request.GET.get('price_max',)
    category_select = request.GET.get('category_select',)
    greader = request.GET.get('greader',)
    minor = request.GET.get('minor',)

    all_categories = Category.objects.all()
    all_products = Product.objects.all()   
    errors = []

    if price_min and price_max and category_select and greader:
        all_products = Product.objects.filter(
        Q(price__gte=price_min) & Q(price__lte=price_max) & Q(categories__name=category_select)
        ).order_by('-price')

    elif price_min and price_max and category_select and minor:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(price__lte=price_max) & Q(categories__name=category_select)
        ).order_by('price')

    elif price_min and price_max and category_select:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(price__lte=price_max) & Q(categories__name=category_select)
        )

    elif price_min and price_max and greader:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(price__lte=price_max)
        ).order_by('-price')

    elif price_min and price_max and minor:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(price__lte=price_max)
        ).order_by('price')

    elif price_min and category_select and greader:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(categories__name=category_select)
        ).order_by('-price')

    elif price_min and category_select and minor:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(categories__name=category_select)
        ).order_by('price')

    elif price_max and category_select and greader:
        all_products = Product.objects.filter(
            Q(price__lte=price_max) & Q(categories__name=category_select)
        ).order_by('-price')

    elif price_max and category_select and minor:
        all_products = Product.objects.filter(
             Q(price__lte=price_max) & Q(categories__name=category_select)
        ).order_by('price')

    elif price_min and price_max:
        try:
            all_products = Product.objects.filter(
                Q(price__gte=price_min) & Q(price__lte=price_max)
            )
        except:
            errors.append('ha ocurrido un errror //')

    elif price_min and category_select:
        all_products = Product.objects.filter(
            Q(price__gte=price_min) & Q(categories__name=category_select)
        )

    elif price_min and greader:
        all_products = Product.objects.filter(
            price__gte=price_min
        ).order_by('-price')

    elif price_min and minor:
        all_products = Product.objects.filter(
        price__gte=price_min
        ).order_by('price')

    elif price_max and category_select:
        all_products = Product.objects.filter(
            Q(price__lte=price_max) & Q(categories__name=category_select)
        )

    elif price_max and greader:
        all_products = Product.objects.filter(
            price__lte=price_max
        ).order_by('-price')

    elif price_max and minor:
        all_products = Product.objects.filter(
            price__lte=price_max
        ).order_by('price')

    elif category_select and greader:
        all_products = Product.objects.filter(
            categories__name=category_select
        ).order_by('-price')

    elif category_select and minor:
        all_products = Product.objects.filter(
            categories__name=category_select
        ).order_by('price')

    elif category_select:
        all_products = Product.objects.filter(
            categories__name=category_select
        )

    elif price_max:
        try:
            all_products = Product.objects.filter(
                price__lte=price_max
            )
        except:
            errors.append('ha ocurrido un errror --')

    elif greader == 'on':
        all_products = Product.objects.all().order_by('-price')

    elif minor == 'on':
        all_products = Product.objects.all().order_by('price')
    
    elif price_min:   
        if price_min is not None and len(price_min) > 0:
            try:
                if int(price_min) < 0:
                    errors.append('Intenta con un valor positivo 😡')
                else:
                    all_products = Product.objects.filter(
                        price__gte=price_min
                    )
            except:
                errors.append('ha ocurrido un errror')

    if len(all_products) == 0:
        errors.append('No se encontro ningun producto relacionado con tu busqueda')

    context = {
        'all_categories': all_categories,
        'all_products': all_products,
        'errors': " ".join(errors),
    }
    return render(request, 'product/multiple_filters.html', context)