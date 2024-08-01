from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Farm, Horse, Employee, TrainingSession
from ..forms.FarmForms import FarmForm

@login_required
def farm_detail(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if not request.user.is_superuser and farm.owner != request.user:
        return redirect('home')
    
    farm.horses = Horse.objects.filter(farm=farm)  # Obtém os cavalos associados à fazenda
    farm.employees = Employee.objects.filter(farm=farm)  # Obtém os funcionários associados à fazenda
    farm.trainingsession_set = TrainingSession.objects.filter(horse__farm=farm, employee__farm=farm)
    return render(request, 'farm/farm_detail.html', {'farm': farm})

@login_required
def add_farm(request):
    if request.method == 'POST':
        form = FarmForm(request.POST)
        if form.is_valid():
            farm = form.save(commit=False)
            farm.owner = request.user
            farm.save()
            return redirect('home')
    else:
        form = FarmForm()
    return render(request, 'farm/operation_farm.html', {'form': form, 'operation': 'Adicionar'})

@login_required
def edit_farm(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = FarmForm(instance=farm)
    return render(request, 'farm/operation_farm.html', {'farm': farm, 'form': form, 'operation': 'Editar'})

@login_required
def delete_farm(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        farm.delete()
        return redirect('home')
    return render(request, 'farm/delete_farm.html', {'farm': farm})

