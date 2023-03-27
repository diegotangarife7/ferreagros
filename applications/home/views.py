from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages


from applications.product.models import Product
from .forms import ContactForm



class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


