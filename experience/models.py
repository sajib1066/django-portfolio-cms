from django.db import models

from account.models import User
from makeportfolio.helper import get_current_user


class Experience(models.Model):
    current_user = get_current_user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    job_title = models.CharField(max_length=220)
    job_context = models.TextField()
    company_name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.job_title

