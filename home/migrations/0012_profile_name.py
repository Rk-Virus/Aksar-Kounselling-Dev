# Generated by Django 4.1.7 on 2023-07-19 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_name_profile_user_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]