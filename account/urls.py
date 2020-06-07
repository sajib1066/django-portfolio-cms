from django.urls import path

from .views import authentication, logout_user, user_profile, profile_setting

urlpatterns = [
    path('', authentication, name='authentication'),
    path('logout/', logout_user, name='logout'),
    path('profile/<int:user_id>', user_profile, name='profile'),
    path('profile/<int:user_id>/settings/', profile_setting, name='profile-setting')
]