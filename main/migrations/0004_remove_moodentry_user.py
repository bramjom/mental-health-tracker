# Generated by Django 5.1 on 2024-09-18 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_moodentry_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='user',
        ),
    ]