from django.urls import path
from rest_proveedor.views import lista_proveedores, crud_proveedores
from rest_proveedor.viewLogin import login

urlpatterns = [
    path('lista_proveedores', lista_proveedores, name="lista_proveedores"),
    path('crud_proveedores/<id>', crud_proveedores, name="crud_proveedores"),
    path('login', login, name="login"),
]   