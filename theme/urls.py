from django.urls import path

from .views import (
    JaksonThemeView,
    AshiaTemplateView,
    ThemeList,
    theme_preview,
    theme_setup,
    theme_setting,
)

urlpatterns = [
    path('jakson/', JaksonThemeView.as_view(), name='jakson'),
    path('ashia/', AshiaTemplateView.as_view(), name='ashia'),
    path('list/', ThemeList.as_view(), name='theme-list'),
    path('preview/<theme_id>', theme_preview, name='theme-preview'),
    path('theme-setup/<theme_id>/', theme_setup, name='theme-setup'),
    path('theme-setting/<int:user_id>', theme_setting, name='theme-setting')
]