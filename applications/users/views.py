from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


from .forms import UserRegisterForm
from .models import User


class UserRegisterForm(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:home')

    def form_valid(self, form):

        user = User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password_1'],
            first_name = form.cleaned_data['first_name'],
            genre = form.cleaned_data['genre']
        )
        return super().form_valid(form)
