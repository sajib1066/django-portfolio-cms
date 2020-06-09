from django.shortcuts import render, redirect

from .models import Education, Experience
from .forms import EducationForm, ExperienceForm

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

def add_experience(request):
    forms = ExperienceForm(request.POST or None)
    if forms.is_valid():
        user = request.user
        job_title = forms.cleaned_data['job_title']
        job_context = forms.cleaned_data['job_context']
        company_name = forms.cleaned_data['company_name']
        start_date = forms.cleaned_data['start_date']
        end_date = forms.cleaned_data['end_date']
        Experience.objects.create(
            user=user,
            job_title=job_title,
            job_context=job_context,
            company_name=company_name,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add-exprience.html', context)

def experience_list(request):
    experience = Experience.objects.filter(user=request.user)
    context = {
        'experience': experience
    }
    return render(request, 'dashboard/experience-list.html', context)