from django.urls import path

from .views import create_education, education_list, add_experience, experience_list

urlpatterns = [
    path('add-education/', create_education, name='education'),
    path('education-list/', education_list, name='education-list'),
    path('add-experience/', add_experience, name='add-experience'),
    path('experience-list/', experience_list, name='experience-list'),
]