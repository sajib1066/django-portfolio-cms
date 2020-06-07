from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from account.models import Theme, SelectedTheme, Profile, User

class DefaultThemeView(TemplateView):
    template_name = 'theme/default/default.html'


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
