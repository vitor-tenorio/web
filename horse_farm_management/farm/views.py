from asyncio import log
from turtle import position
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Employee, Farm, Horse, TrainingSession
from django.contrib.auth.models import User
from .forms import UserForm, TrainingSessionForm

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
    form = UserForm()
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            userName=form['userName'].value()
            firstName=form['firstName'].value()
            lastName=form['lastName'].value()
            email=form['email'].value()
            password=form['senha_1'].value()
            
            if User.objects.filter(username=userName).exists():
                return redirect('cadastro')
            else:
                user = User.objects.create_user(username=userName, first_name=firstName, last_name=lastName, email=email, password=password)
                user.save()
                return redirect('home')
    else:
        form = UserForm()
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
    farm.employees = Employee.objects.filter(farm=farm)  # Obtém os funcionários associados à fazenda
    farm.trainingsession_set = TrainingSession.objects.filter(horse__farm=farm, employee__farm=farm)
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

@login_required
def add_employee(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        name = request.POST['name']
        position = request.POST['position']
    
        employee = Employee(name=name, position=position, farm = farm)
        employee.save()
        #farm.horses.add(horse)
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'add_employee.html', {'farm': farm})

@login_required
def edit_employee(request, farm_id, employee_id):
    farm = get_object_or_404(Farm, id=farm_id)
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.position = request.POST['position']
        employee.save()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'edit_employee.html', {'farm': farm, 'employee': employee})

@login_required
def delete_employee(request, farm_id, employee_id):
    farm = get_object_or_404(Farm, id=farm_id)
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        employee.delete()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'delete_employee.html', {'farm': farm, 'employee': employee})

@login_required
def add_trainingsession(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.method == 'POST':
        form = TrainingSessionForm(request.POST, farm_id=farm_id)
        if form.is_valid():
            training_session = form.save(commit=False)
            training_session.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = TrainingSessionForm(farm_id=farm_id)
    return render(request, 'add_trainingsession.html', {'form': form, 'farm': farm})

@login_required
def edit_trainingsession(request, farm_id, trainingsession_id):
    pass

@login_required
def delete_trainingsession(request, farm_id, trainingsession_id):
    pass