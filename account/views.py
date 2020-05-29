from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm, ProfileForm
from .models import User, Profile

def authentication(request):
    loginforms = LoginForm()
    registrationforms = RegistrationForm()
    if request.method == 'POST':
        loginforms = LoginForm(request.POST)
        registrationforms = RegistrationForm(request.POST)
        if loginforms.is_valid():
            email = loginforms.cleaned_data['email']
            password = loginforms.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
        if registrationforms.is_valid():
            first_name = registrationforms.cleaned_data['first_name']
            last_name = registrationforms.cleaned_data['last_name']
            email = registrationforms.cleaned_data['email']
            password = registrationforms.cleaned_data['password']
            user = User.objects.create_user(email=email, password=password)
            Profile.objects.create(user=user, first_name=first_name, last_name=last_name)
            return redirect('authentication')
            
    context = {
        'login': loginforms,
        'registration': registrationforms
    }
    return render(request, 'dashboard/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authentication')

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    print(user)
    profile = Profile.objects.get(user=user)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
            return redirect('dashboard')
    # forms = ProfileForm()
    context = {
        'forms': forms
    }
    return render(request, 'dashboard/profile.html', context)
