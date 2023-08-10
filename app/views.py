from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView

class SchoolProject(ListView):
    model=School
    context_object_name='SL'



class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'



class  Schoolcreate(CreateView):
    model = School
    fields='__all__'

class Schoolupdate(UpdateView):
    model=School
    fields='__all__'



class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'



