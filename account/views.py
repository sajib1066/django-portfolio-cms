from django.shortcuts import render

def authentication(request):
    return render(request, 'dashboard/login.html')
