from django import forms
from todotask.models import Task

class TaskForm(forms.Form):
    title = forms.CharField(required=False)
    category = forms.CharField(required=False)
    # class Meta:
    #     model = Task
    #     fields = ['title', 'category']
