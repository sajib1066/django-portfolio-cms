from django import forms

from .models import Experience

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
        
    
