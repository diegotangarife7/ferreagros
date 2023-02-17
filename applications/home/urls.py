from django.urls import path

from . import views


app_name="home_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('nosotros/', views.AboutUs.as_view(), name='about_us'),
]
