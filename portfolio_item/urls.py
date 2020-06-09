from django.urls import path

from .views import create_education, education_list

urlpatterns = [
    path('add-education/', create_education, name='education'),
    path('education-list/', education_list, name='education-list'),
]