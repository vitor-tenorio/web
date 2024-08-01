from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Farm
from .viewsFarm import *
from .viewsHorse import *
from .viewsEmployee import *
from .viewsTrainingSession import *
from .viewsUser import *

@login_required
def home(request):
    if request.user.is_superuser:
        farms = Farm.objects.all()
    else:
        farms = Farm.objects.filter(owner=request.user)
    return render(request, 'home.html', {'farms': farms})