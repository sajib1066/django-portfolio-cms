from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect

from account.models import Profile, User
from .forms import SelectedThemeForm
from .models import Theme, SelectedTheme
from portfolio_item.models import (
    Service,
    Education,
    Experience,
    Skill,
    Portfolio
)

class DefaultThemeView(TemplateView):
    template_name = 'theme/default/default.html'


class ThemeList(ListView):
    model = Theme
    template_name = 'theme/theme-list.html'
    context_object_name = 'theme'

def theme_preview(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    context = {
        'th': theme,
        'url': theme.theme_url
    }
    return render(request, 'dashboard/theme-preview.html', context)

def theme_setup(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    usr = User.objects.get(id=request.user.id)
    profile = Profile.objects.get(user=usr)
    try:
        is_theme = SelectedTheme.objects.get(user=usr)
        if is_theme:
            return redirect('dashboard')
    except:
        pass
    SelectedTheme.objects.create(theme=theme, user=usr)
    return redirect('dashboard')

def view_portfolio(request, username):
    profile = Profile.objects.get(username=username)
    user = Profile.objects.get(user=profile.user)
    service = Service.objects.filter(profile=profile)
    education = Education.objects.filter(profile=profile)
    experience = Experience.objects.filter(profile=profile)
    skills = Skill.objects.filter(profile=profile)
    portfolio = Portfolio.objects.filter(profile=profile)
    try:
        theme = SelectedTheme.objects.get(user=user.user)
        context = {
            'profile': profile,
            'service': service,
            'education': education,
            'experience': experience,
            'skills': skills,
            'portfolio': portfolio
        }
        return render(request, f'theme/{theme}/{theme}.html', context)
    except:
        return redirect('theme-list')