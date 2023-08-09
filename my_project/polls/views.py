from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    return render(request, "pages/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def work(request,Day):
    return render(request, "pages/work.html", {"Day":Day})

def joinus(request):
    return render(request, "pages/joinus.html")