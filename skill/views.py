from django.shortcuts import render

from .models import Skill
from .forms import SkillForm

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
