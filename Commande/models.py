from django.db import models

# Create your models here.
class Commande(models.Model):
     STATUS_COMMANDE=(('livré','livré'),('non livré','non livré'))
     items = models.CharField(max_length=300)
     total = models.CharField(max_length=300)
     nom = models.CharField(max_length=150)
     phone =models.CharField(max_length=250,unique=True) 
     email = models.EmailField()
     password = models.CharField(max_length=150)
     adresse = models.CharField(max_length=150)
     ville = models.CharField(max_length=150)
     pays = models.CharField(max_length=150)
     zipcode = models.CharField(max_length=150)
     status=models.CharField(max_length=100,choices=STATUS_COMMANDE)
     date_commande = models.DateTimeField(auto_now_add=True)


     class Meta:
         ordering = ['-date_commande']

     def __str__(self):
         return self.nom

       