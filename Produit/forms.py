from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):

    class Meta:
        model = Produit
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nom du Produit',
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'class': 'form-control',
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'placeholder': 'prix',
                    'class': 'form-control',
                }
            ),
            'quantity': forms.TextInput(
                attrs={
                    'placeholder': 'quantité du produit',
                    'class': 'form-control',
                }
            ),


        }