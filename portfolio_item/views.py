from django.shortcuts import render, redirect

from .models import Education
from .forms import EducationForm

def create_education(request):
    forms = EducationForm(request.POST or None)
    if forms.is_valid():
        user = request.user
        degree = forms.cleaned_data['degree']
        board = forms.cleaned_data['board']
        institute = forms.cleaned_data['institute']
        passing_year = forms.cleaned_data['passing_year']
        result = forms.cleaned_data['result']
        Education.objects.create(
            user=user,
            degree=degree,
            board=board,
            institute=institute,
            passing_year=passing_year,
            result=result
        )
        return redirect('education-list')
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
