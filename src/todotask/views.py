
from django.shortcuts import render, redirect
from todotask.models import Task
from todotask.forms import TaskForm

from todotask.models import Task
# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'todotask/templates/index.html', {'tasks': tasks})

def add_task(request):
    form = TaskForm()
    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('task')
    # else:
    #     form = TaskForm()
    return render(request, 'todotask/templates/add_task.html', {'form': form})
