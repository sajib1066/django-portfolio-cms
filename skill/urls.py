from django.urls import path

from .views import add_skill

urlpatterns = [
    path('add/', add_skill, name='add-skill'),
]