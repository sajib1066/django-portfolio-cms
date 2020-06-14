from django import forms

from .models import SelectedTheme


class SelectedThemeForm(forms.ModelForm):


    class Meta:
        model = SelectedTheme
        fields = ['theme']
        widgets = {
            'theme': forms.Select(attrs={'class': 'form-control'})
        }