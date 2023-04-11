from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages

from applications.product.models import PrincipalProduct, Product
from .forms import ContactForm



class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Principal Product
        principal_product = PrincipalProduct.objects.first()

        price = principal_product.product.price
        discounted_price = principal_product.product.discounted_price

        if discounted_price > 0:
            discount_percentage = 100 - ((discounted_price * 100) / price) 
            context['discount_percentage'] = discount_percentage

        if principal_product.new_product:
            context['new_product'] = 'Producto nuevo'

        context['principal_product_name'] = principal_product.product.name
        context['principal_product_description'] = principal_product.product.description
        context['principal_product_slug'] = principal_product.product.slug
        context['principal_product_principal_image'] = principal_product.product.principal_image


        # featured products and Best sellers (10 images)
        product_images = list(Product.objects.all().order_by('-created')[:9])

        # featured products (4 images)
        featured_products = product_images[:4]
        context['featured_products'] = featured_products
    
        # Best sellers (5 images)
        best_sellers = product_images[4:9]
        context['best_sellers'] = best_sellers
    

        # Contact Form
        context['form'] = ContactForm()
       
        return context
    
    def post(self, request, *args, **kwargs):
        
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            notification = form.cleaned_data['notification']
            if notification ==  False:
                notification = 'El usuario NO desea recibir notificaciones'
            else:
                notification = 'El usuario SI desea recibir notificaciones'
            
            email = EmailMessage(
                'Mensaje FerreAgros formulario: "Contactanos"',
                f'Nombre: {name}\n Correo: {email}\n Teléfono: {phone}\n Asunto: {subject}\n Mensaje: {message}\n Notificaciones: {notification}',
                '', [settings.EMAIL_HOST_USER], reply_to=['email']
            )

            try:
                email.send()
                messages.success(request, 'Tu mensaje ha sido enviado con éxito. Nos comunicaremos contigo lo antes posible. ¡Gracias por contactarnos!')
                return redirect('home_app:home')
            except:
                messages.warning(request, 'Ha ocurrido un error, intenta de nuevo.')
                return redirect('home_app:home')
        else:
            messages.warning(request, 'Ha ocurrido un error, asegúrate de llenar todos los campos correctamente.')
            return redirect('home_app:home')



class AboutUs(TemplateView):
    template_name = 'home/about_us.html'





