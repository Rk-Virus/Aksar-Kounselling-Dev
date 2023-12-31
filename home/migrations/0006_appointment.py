# Generated by Django 4.1.7 on 2023-06-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_user_email_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=255)),
                ('phone_no', models.IntegerField()),
                ('date', models.DateField()),
                ('department', models.TextField()),
                ('doctor', models.TextField()),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]
