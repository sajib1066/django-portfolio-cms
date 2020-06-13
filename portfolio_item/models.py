from django.db import models

from account.models import User, Profile
from makeportfolio.helper import get_user_profile


class About(models.Model):
    user_profile = get_user_profile
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, default=user_profile)
    title = models.CharField(max_length=220)
    about = models.TextField()
    resume = models.FileField(upload_to='resume/')

    def __str__(self):
        return self.title


class Service(models.Model):
    user_profile = get_user_profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=user_profile)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=220)

    def __str__(self):
        return self.name


class Education(models.Model):
    user_profile = get_user_profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=user_profile)
    degree = models.CharField(max_length=220)
    board = models.CharField(max_length=120)
    institute = models.CharField(max_length=220)
    passing_year = models.CharField(max_length=4)
    result = models.DecimalField(max_digits=4, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ['profile', 'degree']

    def __str__(self):
        return self.degree

class Experience(models.Model):
    user_profile = get_user_profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=user_profile)
    job_title = models.CharField(max_length=220)
    job_context = models.TextField()
    company_name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.job_title

class Skill(models.Model):
    user_profile = get_user_profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=user_profile)
    name = models.CharField(max_length=20)
    persent = models.IntegerField()

    def __str__(self):
        return self.name


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    user_profile = get_user_profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=user_profile)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='portfolio/')
    category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=120)
    client_review = models.DecimalField(decimal_places=1, max_digits=3)
    client_feedback = models.TextField()
    budjet = models.PositiveIntegerField()
    duration = models.CharField(max_length=30)
    technology = models.CharField(max_length=120)
    preview = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name

class ContactDetails(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name


