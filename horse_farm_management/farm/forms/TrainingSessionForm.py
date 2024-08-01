from django import forms
from ..models import TrainingSession, Employee, Horse

class AddTrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['horse', 'employee', 'date', 'duration', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'duration': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'horse': forms.Select(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        farm_id = kwargs.pop('farm_id')
        super(AddTrainingSessionForm, self).__init__(*args, **kwargs)
        self.fields['horse'].queryset = Horse.objects.filter(farm_id=farm_id)
        self.fields['employee'].queryset = Employee.objects.filter(farm_id=farm_id)
        
class EditTrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['horse', 'employee', 'date', 'duration', 'notes']
        widgets = {
            'horse': forms.Select(attrs={'readonly': 'readonly','class': 'form-control'}),
            'employee': forms.Select(attrs={'readonly': 'readonly','class': 'form-control'}),
            'date': forms.DateInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'duration': forms.TimeInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditTrainingSessionForm, self).__init__(*args, **kwargs)
        self.fields['horse'].disabled = True
        self.fields['employee'].disabled = True
        self.fields['date'].disabled = True
    
