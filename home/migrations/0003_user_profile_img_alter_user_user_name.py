# Generated by Django 4.1.7 on 2023-04-01 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_user_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='home/images'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
