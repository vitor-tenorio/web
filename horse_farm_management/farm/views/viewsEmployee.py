from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Farm, Employee
from ..forms.EmployeeForms import EmployeeForm

@login_required
def add_employee(request, farm_id):
    farm = get_object_or_404(Farm, id=farm_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.farm = farm
            employee.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = EmployeeForm()
    return render(request, 'employee/operation_employee.html', {'form': form, 'farm': farm, 'operation': 'Adicionar'})

@login_required
def edit_employee(request, farm_id, employee_id):
    farm = get_object_or_404(Farm, id=farm_id)
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.farm = farm
            employee.save()
            return redirect('farm_detail', farm_id=farm.id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/operation_employee.html', {'farm': farm, 'employee': employee, 'form': form, 'operation': 'Editar'})

@login_required
def delete_employee(request, farm_id, employee_id):
    farm = get_object_or_404(Farm, id=farm_id)
    employee = get_object_or_404(Employee, id=employee_id)
    if request.user != farm.owner and not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        employee.delete()
        return redirect('farm_detail', farm_id=farm.id)
    return render(request, 'employee/delete_employee.html', {'farm': farm, 'employee': employee})