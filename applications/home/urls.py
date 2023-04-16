from django.urls import path

from . import views


app_name="home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('nosotros/', views.AboutUsView.as_view(), name='about_us'),


    # admin only
    #path('administrador'/,... ... ... )
    path('about-administrador/', views.AdminAboutView.as_view(), name='about_administrator'),
    path('about-administrador/<int:pk>/', views.AdminAboutEditView.as_view(), name='about_edit'),
]