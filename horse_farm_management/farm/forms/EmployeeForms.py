from django import forms
from ..models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position']
        labels = {
            'name': 'Nome do Empregado',
            'position': 'Cargo do Empregado'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex.: Joao'}),
            'position': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex.: Gerente'}),
        }
    
