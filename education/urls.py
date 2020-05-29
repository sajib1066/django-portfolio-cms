from django.urls import path

from .views import create_education, education_list

urlpatterns = [
    path('', create_education, name='education'),
    path('list/', education_list, name='education-list'),
]