from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Event, Voting

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('creator', 'member', 'event_name', 'location1', 'location2', 'location3', 'time1', 'time2', 'time3', 'end_time')

class VotingForm(forms.ModelForm):
    class Meta:
        model = Voting
        fields = ('event', 'location1_ranking', 'location2_ranking', 'location3_ranking',
                  'time1_ranking', 'time2_ranking', 'time3_ranking')