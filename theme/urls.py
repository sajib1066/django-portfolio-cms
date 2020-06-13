from django.urls import path

from .views import (
    DefaultThemeView,
    AshiaTemplateView,
    ThemeList,
    theme_preview,
    theme_setup
)

urlpatterns = [
    path('', DefaultThemeView.as_view(), name='default-theme'),
    path('ashia/', AshiaTemplateView.as_view(), name='ashia'),
    path('list/', ThemeList.as_view(), name='theme-list'),
    path('preview/<theme_id>', theme_preview, name='theme-preview'),
    path('theme-setup/<theme_id>/', theme_setup, name='theme-setup'),
]