import email
from django import forms
from .models import TrainingSession, Employee, Horse

class TrainingSessionForm(forms.ModelForm):
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
        super(TrainingSessionForm, self).__init__(*args, **kwargs)
        self.fields['horse'].queryset = Horse.objects.filter(farm_id=farm_id)
        self.fields['employee'].queryset = Employee.objects.filter(farm_id=farm_id)
    
class UserForm(forms.Form):
    userName = forms.CharField(
        label="Nome de Usuario",
        required=True,
        max_length=100,
            widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: Joazinho'
                }
            )
    )
    firstName = forms.CharField(
    label="Primeiro Nome",
    required=True,
    max_length=100,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: Joao'
            }
        )
    )
    lastName = forms.CharField(
    label="Sobrenome",
    required=True,
    max_length=100,
        widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: Silva'
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joao@xpto.com'
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    senha_2 = forms.CharField(
        label="Confirmação de Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_2