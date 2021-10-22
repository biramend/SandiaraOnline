from django import forms
from .models import Commande

class CommandeForm(forms.ModelForm):

    class Meta:
        model = Commande
        fields = "__all__"
        widgets = {
            'nom': forms.TextInput(
                attrs={
                    'placeholder': 'Prénom et nom',
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Numéro de téléphone',
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Votre adresse mail',
                    'class': 'form-control',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'placeholder': 'Votre mot de passe',
                    'class': 'form-control',
                }
            ),
            'adresse': forms.TextInput(
                attrs={
                    'placeholder': 'Votre adresse exacte',
                    'class': 'form-control',
                }
            ),
            'ville': forms.TextInput(
                attrs={
                    'placeholder': 'Ville de régidence',
                    'class': 'form-control',
                }
            ),
            'pays': forms.TextInput(
                attrs={
                    'placeholder': 'Votre pays',
                    'class': 'form-control',
                }
            ),


        }