from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Farm, Horse
from ..forms.HorseForms import HorseForm

@login_required
def add_horse(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = HorseForm(request.POST)
        if form.is_valid():
            horse = form.save(commit=False)
            horse.farm = farm
            horse.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = HorseForm()
    return render(request, 'horse/operation_horse.html', {'farm': farm, 'form': form, 'operation': 'Adicionar'})

@login_required
def edit_horse(request, farm_id, horse_id):
    farm = get_object_or_404(Farm, id=farm_id)
    horse = get_object_or_404(Horse, id=horse_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = HorseForm(request.POST, instance=horse)
        if form.is_valid():
            form.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = HorseForm(instance=horse)
    return render(request, 'horse/operation_horse.html', {'farm': farm, 'horse': horse, 'form': form, 'operation': 'Editar'})

@login_required
def delete_horse(request, farm_id, horse_id):
    farm = get_object_or_404(Farm, id=farm_id)
    horse = get_object_or_404(Horse, id=horse_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        horse.delete()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'horse/delete_horse.html', {'farm': farm, 'horse': horse})