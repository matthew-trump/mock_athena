# from django.shortcuts import render
from django.shortcuts import render
# from django.urls import get_resolver
# Create your views here.


def index(request, **kwargs):
   
    return render(request, 'home.html')
