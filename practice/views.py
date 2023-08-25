from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.db.models import Q

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Exercise, Record, User

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

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    return render(request, 'practice/register.html')

class ExerciseForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Describe the exercise..."}), required=False)

    class Meta:
        model = Exercise
        fields = ['name', 'type', 'quality_measurement', 'description', 'skills', 'video_link']

def new_exercise(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
    
    return render(request, 'practice/new_exercise.html', {
        'form': ExerciseForm()
    })

def exercise(request, id):
    exercise = Exercise.objects.filter(id=id).first()
    if exercise:
        return render(request, 'practice/exercise.html', {
            'exercise': exercise,
            'records': Record.objects.filter(Q(exercise=exercise) & Q(user=request.user.id))
        })

def exercises(request):
    return render(request, 'practice/exercises.html', {
        'exercises': Exercise.objects.all()
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
                record.instance.user = User.objects.get(id=request.user.id)
                record.save()

        return render(request, 'practice/record.html', {
            'exercise': exercise,
            'form': RecordForm()
        })