from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

#######################
# EXERCISE PROPERTIES #
#######################

class Type(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name
    
class Measurement(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    
    class Privacy(models.TextChoices):
        PRIV = 'PV', 'Private'
        PUBLIC = 'PB', 'Public'
        UNLISTED = 'UL', 'Unlisted'
    
    name = models.CharField(max_length=100, null=False)
    type = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL, related_name='exercises')
    quality_measurement = models.ForeignKey(Measurement, null=True, on_delete=models.SET_NULL, related_name='exercises')
    description = models.CharField(max_length=500, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='exercises')
    video_link = models.CharField(max_length=64, blank=True, null=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='exercises')
    privacy = models.CharField(max_length=2, choices=Privacy.choices, default="PV")

    def __str__(self):
        return self.name

####################
# PRACTICE ROUTINE #
####################

class Routine(models.Model):

    class Privacy(models.TextChoices):
        PRIV = 'PV', 'Private'
        PUBLIC = 'PB', 'Public'
        UNLISTED = 'UL', 'Unlisted'
    
    name = models.CharField(max_length=100, null=False)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='routines')
    privacy = models.CharField(max_length=2, choices=Privacy.choices, default="PV")
    description = models.CharField(max_length=500, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='routines')


class RoutineExercise(models.Model):
    routine = models.ForeignKey(Routine, related_name='exercises', on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, related_name='routines', on_delete=models.CASCADE)
    length = models.IntegerField()

###########
# RECORDS #
###########

class RoutineRecord(models.Model):
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='records')
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='routine_records', on_delete=models.CASCADE)


class Record(models.Model):
    exercise = models.ForeignKey(Exercise, related_name='records', on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=512, null=True, blank=True)
    quality_rating = models.IntegerField()
    length = models.IntegerField()
    user = models.ForeignKey(User, related_name='records', on_delete=models.CASCADE)
    routine_record = models.ForeignKey(RoutineRecord, related_name='sub_records', on_delete=models.CASCADE, null=True, default=None)