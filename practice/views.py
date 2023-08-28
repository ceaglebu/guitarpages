from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.db.models import Q
from django.db import IntegrityError

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Exercise, Record

# Create your views here.
def index(request):
    return render(request, 'practice/index.html')

def login_view(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'practice/login.html', {
                'message': 'Username or password is incorrect'
            })
    else:
        return render(request, 'practice/login.html')

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, 'practice/register.html', {
                'error': "Passwords do not match"
            })
        
        try:
            user = User.objects.create_user(username, None, password)
            user.save
        except IntegrityError:
            return render(request, 'practice/register.html', {
                'error': 'Username is already taken'
            })

        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'practice/register.html')

def user(request, id):
    return HttpResponse(User.objects.get(id=id))

class ExerciseForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Describe the exercise..."}), required=False)

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'type', 'quality_measurement', 'description', 'skills', 'video_link', 'privacy']

@login_required
def new_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            return HttpResponseRedirect(reverse('exercise', kwargs={'id': form.instance.id}))
    
    return render(request, 'practice/new_exercise.html', {
        'form': ExerciseForm(),
        'action': "Create"
    })

@login_required
def edit_exercise(request, id):
    exercise = Exercise.objects.get(id=id)
    if exercise.creator == request.user:
        if request.method == "POST":
            form = ExerciseForm(request.POST, instance=exercise)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('exercise', kwargs={'id': id}))
            else:
                return render(request, 'practice/new_exercise.html', {
                    'form': form,
                    'action': 'Edit'
                })

        else:
            return render(request, 'practice/new_exercise.html', {
                "form": ExerciseForm(instance=Exercise.objects.get(id=id)),
                'action': 'Edit'
            })
    

def exercise_view(request, id):
    exercise = Exercise.objects.filter(id=id).first()

    if request.user.is_authenticated:
        records = exercise.records.filter(user=request.user.id).order_by('-time')
    else:
        records = None

    if exercise and exercise.creator == request.user or exercise.privacy == "PB" or exercise.privacy == "UL":
        return render(request, 'practice/exercise.html', {
            'exercise': exercise,
            'records': records
        })

def exercises(request):
    if request.user.is_authenticated:
        exercises = Exercise.objects.filter(Q(creator=request.user) | Q(privacy='PB'))
    else:
        exercises = Exercise.objects.filter(privacy='PB')

    return render(request, 'practice/exercises.html', {
        'exercises': exercises
    })

class RecordForm(forms.ModelForm):

    note = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}), required=False)

    class Meta:
        model = Record
        fields = ['note', 'quality_rating', 'length']

def record(request, id):
    exercise = Exercise.objects.filter(id=id).first()
    if exercise:
        
        if request.method == 'POST':
            record = RecordForm(request.POST)
            if record.is_valid():
                record.instance.exercise = exercise
                record.instance.user = request.user
                record.save()

                return HttpResponseRedirect(reverse('exercise', kwargs={'id': id}))

        return render(request, 'practice/record.html', {
            'exercise': exercise,
            'form': RecordForm()
        })