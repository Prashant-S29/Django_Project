from django.contrib import admin
from django.urls import path

from polls import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('work/<Day>/', views.work, name="work"),
    path('joinus/', views.joinus, name="joinus")
    
]
