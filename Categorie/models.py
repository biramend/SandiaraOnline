from django.db import models


# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom
