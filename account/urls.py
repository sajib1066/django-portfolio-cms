from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('registration/', views.user_registration, name='user_registration'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
]