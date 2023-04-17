from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.views.generic.edit import UpdateView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from applications.product.models import PrincipalProduct, Product, ProductImages
from .forms import ContactForm, AboutUsForm
from .models import AboutUs



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


        # featured products and Best sellers (9 images)
        product_images = list(Product.objects.all().order_by('-created')[:9])

        # featured products (4 images)
        featured_products = product_images[:4]
        context['featured_products'] = featured_products

        # Best sellers (5 images)
        best_sellers = product_images[4:9]
        context['best_sellers'] = best_sellers
    

        # Three products random
        three_products = Product.objects.order_by('?')[:3]

        two_products = three_products[:2]
        context['two_products'] = two_products

        one_product = three_products[2:3]
        context['one_product'] = one_product
        
        # Product Images One
        for i in one_product:
            id = i.id
        product_one = Product.objects.get(id=id)
        images_product = ProductImages.objects.filter(product=product_one)
        images_product = images_product[:3]
        context['images_product'] = images_product
        

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



class AboutUsView(TemplateView):
    template_name = 'home/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        information  = AboutUs.objects.last()
        
        context['title'] = information.title
        context['description'] = information.description
        context['principal_image'] = information.principal_image
        context['title_1'] = information.title_1
        context['description_title_1'] = information.description_title_1
        context['avatar'] = information.avatar
        context['name_avatar'] = information.name_avatar
        context['description_avatar'] = information.description_avatar
        context['title_2'] = information.title_2
        context['description_title_2'] = information.description_title_2
        context['title_3'] = information.title_3
        context['description_title_3'] = information.description_title_3        

        return context



# admin only
class AdminView(LoginRequiredMixin, TemplateView):
    login_url = 'users_app:user_login'
    template_name = 'home/administrator.html'



# admin only
class AdminAboutView(LoginRequiredMixin, View):
    login_url = 'users_app:user_login'

    def get(self, request, *args, **kwargs):
        form = AboutUsForm()

        list_about = AboutUs.objects.all().order_by('-created')

        context = {
            'form_about': form,
            'list_about': list_about,
            
        }
        return render(request, 'home/about_admin.html', context)
    

    def post(self, request, *args, **kwargs):

        form = AboutUsForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            principal_image = form.cleaned_data['principal_image']
            title_1 = form.cleaned_data['title_1']
            description_title_1 = form.cleaned_data['description_title_1']
            avatar = form.cleaned_data['avatar']
            name_avatar = form.cleaned_data['name_avatar']
            description_avatar = form.cleaned_data['description_avatar']
            title_2 = form.cleaned_data['title_2']
            description_title_2 = form.cleaned_data['description_title_2']
            title_3 = form.cleaned_data['title_3']
            description_title_3 = form.cleaned_data['description_title_3']
            

            about = AboutUs.objects.create(
                user = request.user,
                title = title,
                description = description,
                principal_image = principal_image,
                title_1 = title_1,
                description_title_1 = description_title_1,
                avatar = avatar, 
                name_avatar = name_avatar,
                description_avatar = description_avatar,
                title_2 = title_2,
                description_title_2 = description_title_2,
                title_3 = title_3,
                description_title_3 = description_title_3
            )
            about.save()
            messages.success(request, 'Se ha creado el \'SOBRE NOSOTROS\' correctamente')
        else:
            messages.warning(request, 'No se pudo procesar tu solicitud. Por favor asegúrate de llenar todos los campos correctamente y vuelve a intentarlo.')

        return redirect('home_app:about_administrator')
            


# admin only
class AdminAboutEditView(LoginRequiredMixin, UpdateView):
    login_url = 'users_app:user_login'
    template_name = 'home/about_edit.html'
    form_class = AboutUsForm
    model = AboutUs
    success_url = reverse_lazy('home_app:about_administrator')

    def form_invalid(self, form):
        messages.warning(self.request, 'No se pudo procesar tu solicitud. Por favor asegúrate de llenar todos los campos correctamente y vuelve a intentarlo.')
        return self.render_to_response(self.get_context_data(form=form))



# admin only
@login_required(login_url='users_app:user_login')
def admin_about_delete(request, id):
    about = AboutUs.objects.get(id=id)
    about.delete()
    return redirect('home_app:about_administrator')

