from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import *
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

now = timezone.now()
#from django.contrib.auth.models import


def home(request):
    return render(request, 'nightout/home.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('NightOut:login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('NightOut:login')

@login_required(login_url='NightOut:login')
def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_date = timezone.now()
            event.save()
            subject = "You are invited"
            message = "You created an event. Tell your friends! They must find the event on NightOut and vote."
            user = request.user
            user_email = user.email
            try:
                send_mail(subject, message, 'nightoutgroup1@gmail.com', [user_email])
                sent = True
            except:
                print("Error sending e-mail")
            return redirect('/')
    else:
        form = EventForm()
    return render(request, 'nightout/create_event.html', {'form': form})

def voting(request, pk):
    event = get_object_or_404(Event, pk=pk)
    events = Event.objects.filter()
    if request.method == "POST":
        form = VotingForm(request.POST)
        if form.is_valid():
            Voting = form.save(commit=False)
            Voting.created_date = timezone.now()
            Voting.save()
            return redirect('/')
    else:
        form = VotingForm
    return render(request, 'nightout/voting.html', {'form': form,
                                                    'events': events,
                                                    })

def event_list(request):
    events = Event.objects.filter()
    voting = Voting.objects.filter()
    return render(request, 'nightout/event_list.html', {'events': events,
                                                        'voting': voting,
                                                        })