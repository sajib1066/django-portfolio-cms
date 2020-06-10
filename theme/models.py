from django.db import models


class Theme(models.Model):
    name = models.CharField(max_length=30, unique=True)
    preview = models.ImageField(upload_to='theme-preview/')
    file_name = models.CharField(max_length=30, unique=True)
    theme_url = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.file_name


class SelectedTheme(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    user = models.ForeignKey('account.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['theme', 'user']

    def __str__(self):
        return self.theme.file_name
