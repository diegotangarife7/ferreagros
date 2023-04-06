from django.urls import path

from . import views


app_name = 'users_app'


urlpatterns = [
    path('registrarse/', views.UserRegisterView.as_view(), name='user_register'),
    path('iniciar-sesion/', views.LoginUser.as_view(), name='user_login'),
    path('cerrar-sesion/', views.LogoutView.as_view(), name='user_logout'),
    path('change-password', views.ChangePassword.as_view(), name='change_password'),
]