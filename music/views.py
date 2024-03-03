from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html',{})