from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from theme.models import Theme

def index_page(request):
    return render(request, 'home/index.html')

@login_required(login_url='authentication')
def dashboard(request):
    theme = Theme.objects.all()
    context = {
        'theme': theme
    }
    return render(request, 'dashboard/index.html', context)