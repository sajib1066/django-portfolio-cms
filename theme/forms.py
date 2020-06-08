from django import forms

from .models import SelectedTheme

class SelectedThemeForm(forms.ModelForm):
    class Meta:
        model = SelectedTheme
        fields = ['theme']