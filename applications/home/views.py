from django.shortcuts import render
from django.views.generic import TemplateView






def home(request):
    return render(request, 'home/home.html')



class AboutUs(TemplateView):
    template_name = 'home/about_us.html'


