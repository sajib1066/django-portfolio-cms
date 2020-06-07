from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm, ProfileForm, SelectedThemeForm
from .models import User, Profile, SelectedTheme

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
            name = first_name + ' ' + last_name
            email = registrationforms.cleaned_data['email']
            password = registrationforms.cleaned_data['password']
            user = User.objects.create_user(email=email, password=password)
            Profile.objects.create(user=user, name=name)
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
    profile = Profile.objects.get(user=user)
    forms = ProfileForm(instance=profile)
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=profile)
        if forms.is_valid():
            forms.save()
    context = {
        'forms': forms
    }
    return render(request, 'dashboard/profile.html', context)

def profile_setting(request, user_id):
    user = User.objects.get(id=user_id)
    select_theme = SelectedTheme.objects.get(user=user)
    forms = SelectedThemeForm(instance=select_theme)
    if request.method == 'POST':
        forms = SelectedThemeForm(request.POST, instance=select_theme)
        if forms.is_valid():
            forms.save()
    context = {
        'theme': select_theme,
        'form': forms
    }
    return render(request, 'dashboard/setting.html', context)
