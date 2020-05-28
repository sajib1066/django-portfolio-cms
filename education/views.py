from django.shortcuts import render, redirect

from .models import Education
from .forms import EducationForm

def education(request):
    forms = EducationForm(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('dashboard')
    context = {
        'forms': forms
    }
    return render(request, 'dashboard/education.html', context)

def education_list(request):
    education = Education.objects.filter(user=request.user)
    print(education)
    context = {
        'education': education
    }
    return render(request, 'dashboard/education-list.html', context)
