from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index_page(request):
    return render(request, 'home/index.html')
@login_required(login_url='authentication')
def dashboard(request):
    return render(request, 'dashboard/index.html')