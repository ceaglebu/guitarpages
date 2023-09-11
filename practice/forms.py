from django import forms
from .models import Exercise, Record, Routine

################
# ExerciseForm #
################

class ExerciseForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Describe the exercise..."}), required=False)

    class Meta:
        model = Exercise
        fields = ['name', 'type', 'quality_measurement', 'description', 'skills', 'video_link', 'privacy']


##############
# RecordForm #
##############

class RecordForm(forms.ModelForm):

    note = forms.CharField(widget=forms.Textarea(attrs={'rows': '4'}), required=False)

    class Meta:
        model = Record
        fields = ['note', 'quality_rating', 'length']


###############
# RoutineForm #
###############

class RoutineForm(forms.ModelForm):

    description = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Describe the routine..."}), required=False)

    class Meta:
        model = Routine
        fields = ['name', 'description', 'skills', 'privacy']