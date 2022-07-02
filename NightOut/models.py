from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


RANK_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

RANK1_CHOICES = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
)

class Creator(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.username)

    @ receiver(post_save, sender=User)
    def create_creator(sender, instance, created, **kwargs):
        if created:
            creator, created = Creator.objects.get_or_create(username=instance)
    post_save.connect(create_creator, sender=User)

class Event(models.Model):
    creator = models.OneToOneField('Creator', on_delete=models.CASCADE, primary_key=True)
    member = models.CharField(max_length=400)
    event_name = models.CharField(max_length=50)
    location1 = models.CharField(max_length=50, null=True)
    location2 = models.CharField(max_length=50, null=True)
    location3 = models.CharField(max_length=50, null=True)
    time1 = models.DateTimeField(default=timezone.now)
    time2 = models.DateTimeField(default=timezone.now)
    time3 = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return str(self.event_name)

class Voting(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)
    location1_ranking = models.IntegerField(choices=RANK_CHOICES, default='0')
    location2_ranking = models.IntegerField(choices=RANK_CHOICES, default='0')
    location3_ranking = models.IntegerField(choices=RANK_CHOICES, default='0')
    time1_ranking = models.IntegerField(choices=RANK1_CHOICES, default='0')
    time2_ranking = models.IntegerField(choices=RANK1_CHOICES, default='0')
    time3_ranking = models.IntegerField(choices=RANK1_CHOICES, default='0')

    def __str__(self):
        return str(self.event)