from django.forms import ModelForm
from .models import Proveedores, Pais

class ProveedoresForm(ModelForm):

    class Meta:
        model = Proveedores
        fields =['idProveedor', 'Nombre', 'Fono', 'Direccion' ,'Mail', 'Pass' ,'IdPais']

class PaisForm(ModelForm):

    class Meta:
        model = Pais
        fields = ['idPais', 'nombrePais']

        