from django.db import models
from Categorie.models import Categorie
from Vendeur.models import Vendeur
from uuid import uuid4

def upload_picture(instance, filename):
    extension = filename.split('.')[-1]
    return 'static/uploads/images/{}.{}'.format(uuid4().hex, extension)
# Create your models here.
class Produit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.DecimalField(max_digits=8,decimal_places=2)
    picture = models.FileField(upload_to=upload_picture, null=True)
    categorie = models.ForeignKey(Categorie,on_delete=models.SET_NULL,null=True)
    vendeur = models.ForeignKey(Vendeur, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name