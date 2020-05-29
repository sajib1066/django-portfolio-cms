from django.urls import path

from .views import add_experience

urlpatterns = [
    path('add/', add_experience, name='add-experience'),
]