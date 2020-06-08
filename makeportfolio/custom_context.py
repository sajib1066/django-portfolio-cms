from theme.models import Theme

def theme_context(request):
    theme = Theme.objects.all()
    context = {
        'theme': theme
    }
    return context