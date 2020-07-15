from account.models import User, Profile
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_current_user():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    user = User.objects.get(id=user_id_list[1])
    return user

def get_user_profile():
    usr = get_current_user()
    profile = Profile.objects.get(user=usr)
    return profile