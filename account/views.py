from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm, ProfileForm
from .models import User, Profile

def user_login(request):
    loginforms = LoginForm()
    if request.method == 'POST':
        loginforms = LoginForm(request.POST)
        if loginforms.is_valid():
            email = loginforms.cleaned_data['email']
            password = loginforms.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            
    context = {
        'login': loginforms,
    }
    return render(request, 'dashboard/auth/user_login.html', context)

def user_registration(request):
    registrationforms = RegistrationForm()
    if request.method == 'POST':
        registrationforms = RegistrationForm(request.POST)
        if registrationforms.is_valid():
            first_name = registrationforms.cleaned_data['first_name']
            last_name = registrationforms.cleaned_data['last_name']
            name = first_name + ' ' + last_name
            email = registrationforms.cleaned_data['email']
            username = registrationforms.cleaned_data['username']
            password = registrationforms.cleaned_data['password']
            confirm_password = registrationforms.cleaned_data['confirm_password']
            if password == confirm_password:
                user = User.objects.create_user(email=email, password=password)
                Profile.objects.create(user=user, name=name, username=username)
            return redirect('user_login')
            
    context = {
        'registration': registrationforms
    }
    return render(request, 'dashboard/auth/user_registration.html', context)

def logout_user(request):
    logout(request)
    return redirect('user_login')

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms,
        'profile': profile
    }
    return render(request, 'dashboard/profile.html', context)
