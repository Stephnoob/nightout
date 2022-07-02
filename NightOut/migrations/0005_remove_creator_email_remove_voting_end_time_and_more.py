# Generated by Django 4.0.5 on 2022-07-01 08:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('NightOut', '0004_creator_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creator',
            name='email',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='end_time',
        ),
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]