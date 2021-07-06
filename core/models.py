from django.db import models

# Create your models here.
class Pais(models.Model):
    idPais = models.IntegerField(primary_key=True, verbose_name="Id de Pais")
    nombrePais = models.CharField(max_length=50, verbose_name="Nombre del Pais")

    def __str__(self):
        return self.nombrePais

class Proveedores(models.Model):
    idProveedor = models.AutoField(primary_key=True, verbose_name="Id de Proveedor")
    Nombre = models.CharField(max_length=100, verbose_name="Nombre Proveedor")
    Fono = models.CharField(max_length=12, verbose_name="Telefóno Proveedor")
    Direccion = models.CharField(max_length=100, verbose_name="Dirección Proveedor")
    Mail = models.CharField(max_length=50, verbose_name="E-mail Proveedor")
    Pass = models.CharField(max_length=20, verbose_name="Password Proveedor")
    IdPais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.Nombre