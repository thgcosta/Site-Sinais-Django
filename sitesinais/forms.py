from django import forms
from django.forms import ModelForm, ValidationError

from .models import CustomUser


class CadastroForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'whatsapp_number',
            'email',
            'referal',
            'password',
        ]

        labels = {
            'first_name': '',
            'last_name': '',
            'whatsapp_number': '',
            'email': '',
            'referal': '',
            'password': '',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'whatsapp_number': forms.NumberInput(attrs={'placeholder': 'Whatsapp'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'referal': forms.TextInput(attrs={'placeholder': 'Codigo Indicação'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError('Já existe um usuário com este email.')
        return email
