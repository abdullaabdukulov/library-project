from django.shortcuts import render, redirect

from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        else:
            messages.error(request, 'Invalid form data.')
            return redirect('accounts:signup')
    form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            user_2 = authenticate(request, email=username, password=password)
            if user or user_2:
                login(request, user)
                return redirect('books:book_list')
            else:
                messages.error(request, 'Invalid username or password.')
                return redirect('accounts:login')
        else:
            messages.error(request, 'Invalid form data.')
            return redirect('accounts:login')
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('accounts:login')
