from django.shortcuts import render

from .forms import LoginForm, RegistrationForm

def authentication(request):
    loginforms = LoginForm()
    registrationforms = RegistrationForm()
    context = {
        'login': loginforms,
        'registration': registrationforms
    }
    return render(request, 'dashboard/login.html', context)
