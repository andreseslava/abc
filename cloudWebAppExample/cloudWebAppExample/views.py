from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth

from django.contrib.auth.models import User
from .forms import LoginForm, CreateUserForm


def landing(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            passw = form.cleaned_data['password']
            authenticatedUser = auth.authenticate(username=user, password=passw)
            if authenticatedUser is not None and authenticatedUser.is_active:
                print("user: " + form.cleaned_data['user'])
                print("password: " + form.cleaned_data['password'])
                auth.login(request, authenticatedUser)
                return HttpResponseRedirect('/events/')
            else:
                return HttpResponseRedirect("account/invalid")
    else:
        form = LoginForm()
    return render(request, 'landing.html', {'form': form})


def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['userName']
            passw = form.cleaned_data['password']
            confirm = form.cleaned_data['confirmPassword']
            print("*******" + user)
            if passw == confirm:
                userCheck = User.objects.create_user(user, user, passw)
                return HttpResponseRedirect("/")
            #TODO add error to GUI

            return HttpResponseRedirect('/register')
        else:
            return HttpResponseRedirect("/createuser")
    else:
        form = CreateUserForm()
    return render(request, 'createUserForm.html', {'form': form})
