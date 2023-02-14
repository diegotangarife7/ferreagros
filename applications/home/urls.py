from django.urls import path

from . import views


app_name="home_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('nosotros/', views.about_us, name='about_us'),
    
]
