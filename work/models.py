from django.db import models

from account.models import User
from makeportfolio.helper import get_current_user


class WorkCategory(models.Model):
    current_user = get_current_user
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=current_user)
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Work(models.Model):
    current_user = get_current_user
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=current_user)
    title = models.CharField(max_length=220)
    link = models.URLField()
    photo = models.ImageField(upload_to='work_photo/')
    description = models.TextField()
    work_category = models.ForeignKey(WorkCategory, on_delete=models.CASCADE)
    source = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()
    client_name = models.CharField(max_length=120)
    client_review = models.DecimalField(decimal_places=1, max_digits=3)
    client_feedback = models.TextField()

    def __str__(self):
        return self.title