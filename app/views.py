from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth import logout as auth_logout

from .models import Customers

# from . import models

def index(request):
    return render(request, "index.html")

def users(request):
    print('Hello')
    return render(request, "users.html")

def create(request):
    return render(request, "create.html")

def logout(request):
    auth_logout(request)
    return redirect(reverse(index))
