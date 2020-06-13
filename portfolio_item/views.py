from django.shortcuts import render, redirect

from account.models import Profile
from .models import (
    About,
    Service,
    Education,
    Experience,
    Skill,
    Portfolio,
    CompletedTask,
    ContactDetails
)
from .forms import (
    AboutForm,
    ServiceForm,
    EducationForm,
    ExperienceForm,
    SkillForm,
    PortfolioForm,
    CompletedTaskForm,
    ContactDetailsForm
)

def create_about(request):
    usr = request.user
    profile = Profile.objects.get(user=usr)
    try:
        about = About.objects.get(profile=profile)
        forms = AboutForm(instance=about)
        if request.method == 'POST':
            forms = AboutForm(request.POST, request.FILES, instance=about)
            if forms.is_valid():
                forms.save()
        context = {
            'form': forms
        }
        return render(request, 'dashboard/about.html', context) 
    except:
        forms = AboutForm()
        if request.method == 'POST':
            forms = AboutForm(request.POST, request.FILES)
            if forms.is_valid():
                forms.save()
        context = {
            'form': forms
        }
        return render(request, 'dashboard/about.html', context)

def add_service_view(request):
    forms = ServiceForm(request.POST or None)
    if forms.is_valid():
        user = request.user
        profile = Profile.objects.get(user=user)
        name = forms.cleaned_data['name']
        description = forms.cleaned_data['description']
        Service.objects.create(
            profile=profile,
            name=name,
            description=description
        )
        return redirect('service')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add-service.html', context)

def service_list_view(request):
    profile = Profile.objects.get(user=request.user)
    service = Service.objects.filter(profile=profile)
    context = {
        'service': service
    }
    return render(request, 'dashboard/service-list.html', context)

def create_education(request):
    forms = EducationForm(request.POST or None)
    if forms.is_valid():
        user = request.user
        profile = Profile.objects.get(user=user)
        degree = forms.cleaned_data['degree']
        board = forms.cleaned_data['board']
        institute = forms.cleaned_data['institute']
        passing_year = forms.cleaned_data['passing_year']
        result = forms.cleaned_data['result']
        Education.objects.create(
            profile=profile,
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
    profile = Profile.objects.get(user=request.user)
    education = Education.objects.filter(profile=profile)
    print(education)
    context = {
        'education': education
    }
    return render(request, 'dashboard/education-list.html', context)

def add_experience(request):
    forms = ExperienceForm(request.POST or None)
    if forms.is_valid():
        profile = Profile.objects.get(user=request.user)
        job_title = forms.cleaned_data['job_title']
        job_context = forms.cleaned_data['job_context']
        company_name = forms.cleaned_data['company_name']
        start_date = forms.cleaned_data['start_date']
        end_date = forms.cleaned_data['end_date']
        Experience.objects.create(
            profile=profile,
            job_title=job_title,
            job_context=job_context,
            company_name=company_name,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('experience-list')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add-exprience.html', context)

def experience_list(request):
    profile = Profile.objects.get(user=request.user)
    experience = Experience.objects.filter(profile=profile)
    context = {
        'experience': experience
    }
    return render(request, 'dashboard/experience-list.html', context)

def add_skill(request):
    forms = SkillForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    profile = Profile.objects.get(user=request.user)
    skill = Skill.objects.filter(profile=profile)
    context = {
        'form': forms,
        'skill': skill
    }
    return render(request, 'dashboard/add-skill.html', context)

def add_portfolio_view(request):
    forms = PortfolioForm()
    if request.method == 'POST':
        forms = PortfolioForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('portfolio-list')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add-portfolio.html', context)

def portfolio_list_view(request):
    profile = Profile.objects.get(user=request.user)
    portfolio = Portfolio.objects.filter(profile=profile)
    context = {
        'portfolio': portfolio
    }
    return render(request, 'dashboard/portfolio-list.html', context)

def completed_task_view(request):
    profile = Profile.objects.get(user=request.user)
    try:
        completed_task = CompletedTask.objects.get(profile=profile)
        forms = CompletedTaskForm(instance=completed_task)
        if request.method == 'POST':
            forms = CompletedTaskForm(request.POST, instance=completed_task)
            if forms.is_valid():
                forms.save()
    except:
        forms = CompletedTaskForm(request.POST or None)
        if forms.is_valid():
            forms.save()
    context = {
        'form': forms
    }
    return render(request, 'dashboard/completed-task.html', context)

def contact_details_view(request):
    profile = Profile.objects.get(user=request.user)
    try:
        contact_details = ContactDetails.objects.get(profile=profile)
        forms = ContactDetailsForm(instance=contact_details)
        if request.method == 'POST':
            forms = ContactDetailsForm(request.POST, instance=contact_details)
            if forms.is_valid():
                forms.save()
    except:
        forms = ContactDetailsForm()
        if request.method == 'POST':
            forms = ContactDetailsForm(request.POST)
            if forms.is_valid():
                forms.save()
    context = {
        'form': forms
    }
    return render(request, 'dashboard/contact-details.html', context)