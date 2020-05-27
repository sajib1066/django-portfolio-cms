from django.urls import path

from .views import authentication, logout_user

urlpatterns = [
    path('', authentication, name='authentication'),
    path('logout/', logout_user, name='logout')
]