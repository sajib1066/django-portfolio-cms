from django import forms

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


class AboutForm(forms.ModelForm):


    class Meta:
        model = About
        exclude = ('profile',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):


    class Meta:
        model = Service
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class EducationForm(forms.ModelForm):


    class Meta:
        model = Education
        fields = ['degree', 'board', 'institute', 'passing_year', 'result']

        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your degree title'}),
            'board': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your board name'}),
            'institute': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your institute name'}),
            'passing_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your passing year'}),
            'result': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your result'}),
        }


class ExperienceForm(forms.ModelForm):


    class Meta:
        model = Experience
        exclude = ('user', )

        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Job Title'}),
            'job_context': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Job Context'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class SkillForm(forms.ModelForm):


    class Meta:
        model = Skill
        fields = ['name', 'persent']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'persent': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class PortfolioForm(forms.ModelForm):


    class Meta:
        model = Portfolio
        exclude = ('profile', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_review': forms.TextInput(attrs={'class': 'form-control'}),
            'client_feedback': forms.TextInput(attrs={'class': 'form-control'}),
            'budjet': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'technology': forms.TextInput(attrs={'class': 'form-control'}),
            'preview': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CompletedTaskForm(forms.ModelForm):


    class Meta:
        model = CompletedTask
        fields = ['projects', 'clients', 'partners', 'cup_of_coffee']

        widgets = {
            'projects': forms.NumberInput(attrs={'class': 'form-control'}),
            'clients': forms.NumberInput(attrs={'class': 'form-control'}),
            'partners': forms.NumberInput(attrs={'class': 'form-control'}),
            'cup_of_coffee': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ContactDetailsForm(forms.ModelForm):


    class Meta:
        model = ContactDetails
        fields = ['name', 'email', 'phone', 'address']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'})
        }
