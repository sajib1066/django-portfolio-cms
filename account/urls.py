from django.urls import path

from .views import authentication

urlpatterns = [
    path('', authentication, name='authentication'),
]