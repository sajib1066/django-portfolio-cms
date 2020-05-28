from django.urls import path

from .views import education, education_list

urlpatterns = [
    path('', education, name='education'),
    path('list/', education_list, name='education-list'),
]