from django.urls import path

from .views import (
    create_about,
    add_service_view,
    service_list_view,
    create_education,
    education_list,
    add_experience,
    experience_list,
    add_skill
)

urlpatterns = [
    path('about/', create_about, name='add-about'),
    path('add-service/', add_service_view, name='add-service'),
    path('service/', service_list_view, name='service'),
    path('add-education/', create_education, name='education'),
    path('education-list/', education_list, name='education-list'),
    path('add-experience/', add_experience, name='add-experience'),
    path('experience-list/', experience_list, name='experience-list'),
    path('add-skill/', add_skill, name='add-skill'),
]