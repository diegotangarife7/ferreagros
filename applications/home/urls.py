from django.urls import path

from . import views


app_name="home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('nosotros/', views.AboutUsView.as_view(), name='about_us'),
]