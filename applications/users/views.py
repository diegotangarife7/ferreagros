from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import UserRegisterForm, LoginForm, UpdatePasswordForm
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
        login(self.request, user)
        return redirect(self.success_url)    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
            


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):
        user = authenticate(
            email = form.cleaned_data['email'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)



class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home_app:home')
    


class ChangePassword(LoginRequiredMixin, FormView):
    login_url = 'users_app:user_login'
    template_name = 'users/change_password.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:user_login')

    def form_valid(self, form):
        user = self.request.user

        if user.check_password(form.cleaned_data['old_password']):
            new_password = form.cleaned_data['new_password_1']
            user.set_password(new_password)
            user.save()
        else:
            #form.add_error('old_password', 'La contraseña que proporcionaste no coincide con la contraseña actual. Por favor, intenta de nuevo con la contraseña correcta.')
            messages.error(self.request, 'La contraseña que proporcionaste no coincide con la contraseña actual. Por favor, intenta de nuevo con la contraseña correcta.')
            return self.form_invalid(form)

        logout(self.request)
        messages.success(self.request, '¡Listo! Tu contraseña ha sido cambiada con éxito. Inicia sesión')
        return super().form_valid(form)
    