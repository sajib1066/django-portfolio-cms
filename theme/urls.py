from django.urls import path

from .views import DefaultThemeView
from .views import theme_preview

urlpatterns = [
    path('', DefaultThemeView.as_view(), name='default-theme'),
    path('preview/<theme_id>', theme_preview, name='theme-preview'),
]