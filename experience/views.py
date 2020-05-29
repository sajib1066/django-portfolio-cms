from django.shortcuts import render, redirect

from .models import Experience
from .forms import ExperienceForm

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
        'forms': forms
    }
    return render(request, 'dashboard/add-exprience.html', context)
