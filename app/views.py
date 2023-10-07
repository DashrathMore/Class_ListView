from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView

from app.models import *

class listview(ListView):
    model=Student
    template_name='listview.html'
    context_object_name='slist'