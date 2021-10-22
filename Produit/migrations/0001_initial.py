# Generated by Django 3.2.7 on 2021-09-12 09:56

import Produit.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vendeur', '0001_initial'),
        ('Categorie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('picture', models.FileField(null=True, upload_to=Produit.models.upload_picture)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Categorie.categorie')),
                ('vendeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Vendeur.vendeur')),
            ],
        ),
    ]
