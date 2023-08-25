from django.contrib import admin

from .models import Type, Skill, Exercise, Measurement, Record

# Register your models here.
for model in [Type, Skill, Exercise, Measurement, Record]:
    admin.site.register(model)