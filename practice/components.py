from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import Q

from .models import Exercise

def add_exercise(request):
    return JsonResponse({'body': render_to_string(request=request, template_name="practice/components/add_exercise.html", context={
        "exercises": Exercise.objects.filter(Q(creator=request.user) | Q(privacy='PB'))
    })})