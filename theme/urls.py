from django.urls import path

from .views import DefaultThemeView

urlpatterns = [
    path('', DefaultThemeView.as_view(), name='default-theme'),
]