from django import forms
from .models import Vendeur

class VendeurForm(forms.ModelForm):
    class Meta:
        model = Vendeur
        fields = "__all__"

        widgets = {
            'nom': forms.TextInput(
                attrs={
                    'placeholder': 'Nom du vendeur',
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Ex:biramendiaye@gmail.com',
                    'class': 'form-control',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Ex:+221768623263',
                    'class': 'form-control',
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'placeholder': 'Ex:Dakar',
                    'class': 'form-control',
                }
            ),
            'nci': forms.TextInput(
                attrs={
                    'placeholder': 'Ex:1710200100124',
                    'class': 'form-control',
                }
            ),
        }