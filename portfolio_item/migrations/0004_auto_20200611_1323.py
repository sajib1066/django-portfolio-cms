# Generated by Django 3.0.6 on 2020-06-11 13:23

from django.db import migrations, models
import django.db.models.deletion
import makeportfolio.helper


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_profile_about'),
        ('portfolio_item', '0003_auto_20200611_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='user',
            field=models.OneToOneField(default=makeportfolio.helper.get_user_profile, on_delete=django.db.models.deletion.CASCADE, to='account.Profile'),
        ),
    ]