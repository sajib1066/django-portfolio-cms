from django.views.generic import TemplateView

class DefaultThemeView(TemplateView):
    template_name = 'theme/default/default.html'
