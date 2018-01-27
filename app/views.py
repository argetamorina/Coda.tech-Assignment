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
        # Do something for authenticated users.
        current_user = request.user
        # print (current_user.first_name)
    # else:
        # Do something for anonymous users.

    context = {
        'customers': Customer.objects.all()
    }
    return render(request, "users.html", context)

def create(request):
    if request.method == 'POST':
        # print(request.POST['first_name'])
        # print(Customer.objects.all())
        if request.user.is_authenticated():
            customer = models.Customer.objects.validation(first_name=request.POST['first_name'], last_name=request.POST['last_name'], iban=request.POST['iban'], administrator = request.user)
            print(customer[1])
            if customer[0]:
                request.session['user'] = customer[1]
                return redirect(reverse(users))
            else:
                context = {
                    'errors': customer[1],
                    'class': 'is-invalid'
                }
                return render(request, 'create.html', context)
        # print("hej qitu jom 2")
        return redirect(reverse('users'))
    return render(request, "create.html")

def update(request, id):

    return redirect(reverse('users'))

def destroy(request, id):
    if request.user.is_authenticated():
        administrator = User.objects.get(id=request.user.id)

        Customer.objects.remove(administrator=administrator.id, customer=id)

    return redirect(reverse('users'))

def logout(request):
    auth_logout(request)
    return redirect(reverse(index))
