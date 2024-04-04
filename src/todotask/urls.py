
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="task-index"),
    path('add/', add_task, name='add_task'),
]