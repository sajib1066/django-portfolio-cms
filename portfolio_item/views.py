from django.shortcuts import render, redirect

from account.models import Profile
from .models import About, Service, Education, Experience, Skill
from .forms import AboutForm, ServiceForm, EducationForm, ExperienceForm, SkillForm

def create_about(request):
    usr = request.user
    profile = Profile.objects.get(user=usr)
    try:
        about = About.objects.get(user=profile)
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
        name = forms.cleaned_data['name']
        description = forms.cleaned_data['description']
        Service.objects.create(
            user=user,
            name=name,
            description=description
        )
        return redirect('dashboard')
    context = {
        'form': forms
    }
    return render(request, 'dashboard/add-service.html', context)

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

def add_skill(request):
    forms = SkillForm(request.POST or None)
    if forms.is_valid():
        user = request.user
        name = forms.cleaned_data['name']
        persent = forms.cleaned_data['persent']
        Skill.objects.create(user=user, name=name, persent=persent)
    
    skill = Skill.objects.filter(user=request.user)
    context = {
        'form': forms,
        'skill': skill
    }
    return render(request, 'dashboard/add-skill.html', context)