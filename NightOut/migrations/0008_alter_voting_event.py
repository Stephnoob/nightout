# Generated by Django 4.0.5 on 2022-07-01 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NightOut', '0007_alter_event_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='NightOut.event'),
        ),
    ]
