# Generated by Django 3.1.4 on 2021-10-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('total', models.CharField(max_length=300)),
                ('nom', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=150)),
                ('adresse', models.CharField(max_length=150)),
                ('ville', models.CharField(max_length=150)),
                ('pays', models.CharField(max_length=150)),
                ('zipcode', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('livré', 'livré'), ('non livré', 'non livré')], max_length=100)),
                ('date_commande', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_commande'],
            },
        ),
    ]