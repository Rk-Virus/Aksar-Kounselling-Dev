# Generated by Django 4.1.7 on 2023-08-05 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_delete_appointment2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='appointment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.appointment'),
        ),
    ]