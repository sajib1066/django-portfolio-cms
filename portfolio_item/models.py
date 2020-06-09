from django.db import models

from account.models import User
from makeportfolio.helper import get_current_user

class Education(models.Model):
    current_user = get_current_user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    degree = models.CharField(max_length=220)
    board = models.CharField(max_length=120)
    institute = models.CharField(max_length=220)
    passing_year = models.CharField(max_length=4)
    result = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['user', 'degree']

    def __str__(self):
        return self.degree

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

class Skill(models.Model):
    current_user = get_current_user
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=current_user)
    name = models.CharField(max_length=20)
    persent = models.IntegerField()

    def __str__(self):
        return self.name

