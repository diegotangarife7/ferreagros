from django.urls import path

from . import views


app_name = 'users_app'


urlpatterns = [
    path('registrarse/', views.UserRegisterForm.as_view(), name='user_register')
]
