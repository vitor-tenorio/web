from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Farm, TrainingSession
from ..forms.TrainingSessionForm import AddTrainingSessionForm, EditTrainingSessionForm

@login_required
def add_trainingsession(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.method == 'POST':
        form = AddTrainingSessionForm(request.POST, farm_id=farm_id)
        if form.is_valid():
            training_session = form.save(commit=False)
            training_session.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = AddTrainingSessionForm(farm_id=farm_id)
    return render(request, 'trainingsession/operation_trainingsession.html', {'form': form, 'farm': farm, 'operation': 'Adicionar'})

@login_required
def edit_trainingsession(request, farm_id, trainingsession_id):
    farm = get_object_or_404(Farm, id=farm_id)
    session = get_object_or_404(TrainingSession, id=trainingsession_id)
    if request.method == 'POST':
        form = EditTrainingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = EditTrainingSessionForm(instance=session)
    return render(request, 'trainingsession/operation_trainingsession.html', {'form': form, 'farm': farm, 'session': session, 'operation': 'Editar'})

@login_required
def delete_trainingsession(request, farm_id, trainingsession_id):
    farm = get_object_or_404(Farm, id=farm_id)
    session = get_object_or_404(TrainingSession, id=trainingsession_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        session.delete()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'trainingsession/delete_trainingsession.html', {'farm': farm, 'session': session})