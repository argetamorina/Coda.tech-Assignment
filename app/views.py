from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from . import models



from .models import Customer


def index(request):
    print(User.objects.all())
    # request.session['user'] = User.objects.filter(user)

    return render(request, "index.html")

def users(request):
    print('Hello')
    print(User.objects.get())
    if request.user.is_authenticated():
    # Do something for authenticated users.
        print(request.user.is_authenticated())
        current_user = request.user
        print (current_user.first_name)
    else:
    # Do something for anonymous users.
        print('qitu jom ')
    context = {
        'customers': Customer.objects.all()
    }
    return render(request, "users.html", context)

def create(request):
    if request.method == 'POST':
        # print(request.POST['first_name'])
        print(Customer.objects.all())
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
        print("hej qitu jom 2")
        return redirect(reverse('users'))
    return render(request, "create.html")

def logout(request):
    auth_logout(request)
    return redirect(reverse(index))
