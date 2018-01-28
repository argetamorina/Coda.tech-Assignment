from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from . import models
from .models import Customer


def index(request):

    return render(request, "index.html")

def users(request):
    if request.user.is_authenticated():
        current_user = request.user
    else:
        return redirect(reverse(index))
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, "users.html", context)

def create(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            customer = models.Customer.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], iban=request.POST['iban'], administrator = request.user)
            # False
            if customer[0]:
                return redirect(reverse(users))
            else:
                context = {
                    'errors': customer[1],
                    'class': 'is-invalid'
                }
                return render(request, 'create.html', context)
        else:
            return redirect(reverse(index))
    return render(request, "create.html")

def update(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated():
            administrator = User.objects.get(id=request.user.id)
            update = Customer.objects.update(administrator=administrator.id, customer=id, first_name=request.POST['first_name'], last_name=request.POST['last_name'], iban=request.POST['iban'])
            print(update[0])
            if update[0]:
                return redirect(reverse(users))
            else:
                context = {
                    'errors': update[1],
                    'class': 'is-invalid',
                }
                return render(request, 'update.html', context)

        else:
                return redirect(reverse(index))

        return redirect(reverse(index))
    context = {
        'customer': Customer.objects.get(id=id)
    }
    return render(request, 'update.html', context)

def destroy(request, id):
    if request.user.is_authenticated():
        administrator = User.objects.get(id=request.user.id)

        Customer.objects.remove(administrator=administrator.id, customer=id)

    return redirect(reverse('users'))

def logout(request):
    # auth_logout(request)
    return redirect(reverse(index))
