# Generated by Django 4.1.7 on 2023-04-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact_rename_user_dob_user_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=50),
        ),
    ]
