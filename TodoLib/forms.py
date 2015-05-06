from django import forms
from .models import Task
from django.core.exceptions import ValidationError


class TaskChecker(forms.ModelForm):
    class Meta:
            model = Task
            fields = ['title','description','deadline','status']
            
   
    status = forms.IntegerField(label='status')

    def clean_status(self):
        status = self.cleaned_data['status']
        print status
        if status > 100 or status < 0:
            raise ValidationError('Please enter a value from 0-100')
        return status