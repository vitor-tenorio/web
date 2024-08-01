from django import forms
from ..models import Horse

class HorseForm(forms.ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'breed','age']
        labels = {
            'name': 'Nome',
            'breed': 'Raça',
            'age': 'Idade',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex.: Pé de Pano'}),
            'breed': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ex.: Mangalarga Marchador'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ex.: 5'})
        }
    
