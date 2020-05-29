from django.urls import path

from .views import authentication, logout_user, user_profile

urlpatterns = [
    path('', authentication, name='authentication'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:user_id>', user_profile, name='profile')
]