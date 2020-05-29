from django import forms

from .models import Education

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