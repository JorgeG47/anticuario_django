# Generated by Django 4.1.2 on 2023-07-04 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAnticuario', '0002_producto_imagen_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_prod',
            field=models.ImageField(upload_to='productos'),
        ),
    ]
