from django import forms
from .models import Diary

class PostForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('record_date' ,'meal_type', 'meal_time', 'meal_contents',
                  'medicine_time', 'medicine_contents', 'pain', 'pain_degree', 'condition')

