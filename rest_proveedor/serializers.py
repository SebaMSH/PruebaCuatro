from rest_framework import serializers
from core.models import Proveedores, Pais

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields =['idProveedor', 'Nombre', 'Fono', 'Direccion' ,'Mail', 'Pass' ,'IdPais']
    
class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['idPais', 'nombrePais']
        
