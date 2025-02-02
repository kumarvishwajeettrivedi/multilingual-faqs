from django.contrib import admin
from django.urls import path, include 
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the FAQ system!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('faq_app.urls')), 
    path('', home, name='home'),  
]
