# Generated by Django 3.0.6 on 2020-06-08 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200607_0532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=30, unique=True),
            preserve_default=False,
        ),
    ]