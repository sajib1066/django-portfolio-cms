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
    profile = Profile.objects.get(user=request.user)
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
                return redirect('dashboard')
        context = {
            'form': forms
        }
        return render(request, 'dashboard/about.html', context)

def add_service_view(request):
    forms = ServiceForm(request.POST or None)
    if forms.is_valid():
        forms.save()
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
        forms.save()
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
        forms.save()
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