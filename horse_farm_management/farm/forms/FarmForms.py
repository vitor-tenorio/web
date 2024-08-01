from django import forms
from ..models import Farm

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ['name', 'location']
        labels = {
            'name': 'Nome',
            'location': 'Localização',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex.: Farm of Dreams'}),
            'location': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex.: Lavras, MG'}),
        }
    
