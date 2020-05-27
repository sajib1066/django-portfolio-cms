from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm, RegistrationForm

def authentication(request):
    loginforms = LoginForm()
    registrationforms = RegistrationForm()
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
        'registration': registrationforms
    }
    return render(request, 'dashboard/login.html', context)
