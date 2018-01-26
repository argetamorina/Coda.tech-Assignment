from django.shortcuts import render, redirect
# from . import models

def index(request):
    return render(request, "index.html")

def users(request):
    print('Hello')
    return render(request, "users.html")
