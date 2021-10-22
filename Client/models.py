from django.db import models

# Create your models here.
class Client(models.Model):
    prenom=models.CharField(max_length=100,verbose_name="Prenom et Nom")
    adresse = models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=200)
    phone=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=200,unique=True)


    def __str__(self):
        return self.prenom