from django import forms
from .models import Habit, DailyRecord

class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'metric', 'unit_of_measure', 'description')

class DailyRecordForm(forms.ModelForm):
    
    class Meta:
        model = DailyRecord
        fields = ('habit', 'date', 'amount_completed')