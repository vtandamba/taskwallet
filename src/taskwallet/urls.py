"""
URL configuration for task project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, connexion
from todotask.views import index as task_index
from todotask.views import add_task
from wallet.views import index as wallet_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('task/', task_index),
    path('task-add/', add_task),
    path('wallet/', wallet_index),
    path('connexion/', connexion),
    # path("services/", views.services, name="services"),
    # path("connexion/", views.connexion, name="connexion"),
    # path("contact/", views.contact, name="contact"),
]
