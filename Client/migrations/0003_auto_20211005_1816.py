# Generated by Django 3.1.4 on 2021-10-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_auto_20210915_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]