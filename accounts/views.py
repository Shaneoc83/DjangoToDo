from django.shortcuts import render, redirect
from forms import UserLoginForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from accounts.forms import UserRegistrationForm
from django.contrib import messages, auth
from django.conf import settings


import json
from django.views.decorators.csrf import csrf_exempt
from models import User
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                return redirect(reverse('index'))
            else:
                form.add_error(None, "Your username or password was not recognised")
    else:
        form = UserLoginForm()

    args = {'form': form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password1'))

            if user:
                messages.success(request, "you have successfully registered, big woop.")
                auth.login(request, user)
                print ("hihihhihihih")
                return redirect(reverse('index'))
            else:
                print ("hi")
                messages.error(request, "unable to log you in at this time!")


    else:
        form = UserRegistrationForm()
        print ("hi-hooooo")
    args = {'form': form}
    args.update(csrf(request))

    return render(request, 'register.html', args)
