from django.urls import path

from .views import add_experience, experience_list

urlpatterns = [
    path('add/', add_experience, name='add-experience'),
    path('list/', experience_list, name='experience-list'),
]