# Generated by Django 4.1.2 on 2023-07-04 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAnticuario', '0003_alter_producto_imagen_prod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_prod',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio_prod',
            field=models.IntegerField(),
        ),
    ]