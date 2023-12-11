from django.db import models
# Create your models here.

class producto(models.Model):
    id_prod =  models.IntegerField(primary_key=True)
    id_prod_etiqueta = models.CharField(max_length=15)
    enOferta = models.BooleanField(default=False)
    imagen_prod = models.ImageField(upload_to="productos")
    nom_prod = models.CharField(max_length=35)
    precio_prod = models.IntegerField()
    desc_prod= models.CharField(max_length=150)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.nom_prod} -> {self.precio_prod}'
    

    