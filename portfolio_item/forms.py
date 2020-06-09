from django import forms

from .models import Education, Experience

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
            'start_date': forms.TextInput(attrs={'class': 'form-control'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control'}),
        }
        