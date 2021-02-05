
from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name="home"),
   path('index.html', views.index, name="index"),
   path('contact.html', views.contact, name="contact"),
   path('about.html', views.about, name="about"),
   path('project.html', views.project, name="project"),
   path('services.html', views.services, name="services"),
   path('appointment.html', views.appointment, name="appointment"),
  
]