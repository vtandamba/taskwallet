from datetime import datetime

from django.shortcuts import render


def index(request):
    return render(request, 'taskwallet/templates/index.html', context={"date": datetime.today()})