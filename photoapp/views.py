from django.shortcuts import render
from twitter import *
from tkinter import *


def index(request):
    return render(request, 'photoapp/home.html')


def tweet(request):
    return render(request, 'photoapp/home.html')
