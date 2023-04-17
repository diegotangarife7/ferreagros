from django.urls import path

from . import views


app_name="home_app"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('nosotros/', views.AboutUsView.as_view(), name='about_us'),

    # admin only
    path('administrador/', views.AdminView.as_view(), name='administrator'),
    path('administrador-about/', views.AdminAboutView.as_view(), name='about_administrator'),
    path('administrador-about/<int:pk>/editar/', views.AdminAboutEditView.as_view(), name='about_edit'),
    path('administrador-about/<int:id>/borrar/', views.admin_about_delete, name='about_delete'),
]