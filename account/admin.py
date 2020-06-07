from django.contrib import admin
from .models import User, Profile, Theme, SelectedTheme

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Theme)
admin.site.register(SelectedTheme)