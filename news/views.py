from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

# Create your views here.


class Home(ListView):
    model = Posts
    template_name = "home.html"