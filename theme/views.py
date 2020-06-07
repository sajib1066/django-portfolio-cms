from django.views.generic import TemplateView
from django.shortcuts import render

from account.models import Theme

class DefaultThemeView(TemplateView):
    template_name = 'theme/default/default.html'


def theme_preview(request, theme_id):
    theme = Theme.objects.get(id=theme_id)
    context = {
        'th': theme,
        'url': theme.theme_url
    }
    return render(request, 'dashboard/theme-preview.html', context)