from django.urls import path

from . import views


app_name = 'users_app'


urlpatterns = [
    path('registrarse/', views.UserRegisterFormView.as_view(), name='user_register')
]
