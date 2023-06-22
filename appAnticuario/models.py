from django.db import models
# Create your models here.

class producto(models.Model):
    id_prod =  models.IntegerField(primary_key=True, max_length=5)
    id_prod_etiqueta = models.CharField(max_length=15)
   # """ id_oferta= models.ForeignKey('En oferta', on_delete=models.CASCADE, db_column='') """
    nom_prod = models.CharField(max_length=35)
    precio_prod = models.IntegerField(max_length=7)
    desc_prod= models.CharField(max_length=150)
    cantidad = models.IntegerField(max_length=3)



#""" class ofertas(models.model): """
    