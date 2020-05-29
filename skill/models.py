from django.db import models
from account.models import User

from makeportfolio.helper import get_current_user

class MySkill(models.Model):
    current_user = get_current_user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    name = models.CharField(max_length=20)
    persent = models.IntegerField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    current_user = get_current_user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    about = models.TextField()
    skills = models.ManyToManyField(MySkill)

    def __str__(self):
        return self.about[10]
