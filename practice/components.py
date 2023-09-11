from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from .models import Exercise
from .forms import ExerciseForm

def add_exercise(request):
    return JsonResponse({'body': render_to_string(request=request, template_name="practice/components/add_exercise.html", context={
        "exercises": Exercise.objects.filter(Q(creator=request.user) | Q(privacy='PB'))
    })})

def new_exercise_form(request):
    return JsonResponse({'body': render_to_string(request=request, template_name="practice/components/new_exercise_form.html", context={
        "form": ExerciseForm(auto_id='exercise_%s')
    })})

def existing_added_exercise(request, id):
    return JsonResponse({'body': render_to_string(request=request, template_name='practice/components/added_exercise.html', context={
        'exercise': Exercise.objects.get(id=id) 
    })})