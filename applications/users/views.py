from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import redirect


from .forms import UserRegisterForm
from .models import User

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['name'],
            form.cleaned_data['password1']  
        )
        return redirect(self.success_url)    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
            
