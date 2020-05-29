from django import forms

from .models import Skill

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'persent']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'persent': forms.NumberInput(attrs={'class': 'form-control'}),
        }