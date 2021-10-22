from django.db import models
from uuid import uuid4

def upload_profile(instance, filename):
    extension = filename.split('.')[-1]
    return 'static/uploads/profiles/{}.{}'.format(uuid4().hex, extension)
# Create your models here.
class Vendeur(models.Model):
    nom = models.CharField(max_length=100,verbose_name='Prénom et nom')
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True,max_length=200)
    address = models.CharField(max_length=200)
    nci =models.CharField(max_length=200,unique=True,verbose_name='Numéro carte d\'identité')
    profile = models.FileField(upload_to=upload_profile, null=True)

    def __str__(self):
        return self.nom

