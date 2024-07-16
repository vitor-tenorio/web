from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Farm, Horse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def add_user(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'add_user.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    if request.user.is_superuser:
        farms = Farm.objects.all()
    else:
        farms = Farm.objects.filter(owner=request.user)
    return render(request, 'home.html', {'farms': farms})

@login_required
def farm_detail(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if not request.user.is_superuser and farm.owner != request.user:
        return redirect('home')
    
    farm.horses = Horse.objects.filter(farm=farm)  # Obtém os cavalos associados à fazenda
    return render(request, 'farm_detail.html', {'farm': farm})

@login_required
def add_farm(request):
    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        farm = Farm(name=name, location=location, owner=request.user)
        farm.save()
        return redirect('home')
    return render(request, 'add_farm.html')

@login_required
def edit_farm(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        farm.name = request.POST['name']
        farm.location = request.POST['location']
        farm.save()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'edit_farm.html', {'farm': farm})

@login_required
def delete_farm(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        farm.delete()
        return redirect('home')
    return render(request, 'delete_farm.html', {'farm': farm})

@login_required
def add_horse(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST['name']
        breed = request.POST['breed']
        age = request.POST['age']
        horse = Horse(name=name, breed=breed, age=age, farm = farm)
        horse.save()
        #farm.horses.add(horse)
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'add_horse.html', {'farm': farm})

@login_required
def edit_horse(request, farm_id, horse_id):
    farm = get_object_or_404(Farm, id=farm_id)
    horse = get_object_or_404(Horse, id=horse_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        horse.name = request.POST['name']
        horse.breed = request.POST['breed']
        horse.age = request.POST['age']
        horse.save()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'edit_horse.html', {'farm': farm, 'horse': horse})

@login_required
def delete_horse(request, farm_id, horse_id):
    farm = get_object_or_404(Farm, id=farm_id)
    horse = get_object_or_404(Horse, id=horse_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        horse.delete()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'delete_horse.html', {'farm': farm, 'horse': horse})
