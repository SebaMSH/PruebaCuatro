from django.urls import path
from .views import index , dulce, salada, mixta, contacto, nosotros, sismos, home, ingreso_proveedor, ingreso_pais, listar_proveedor, form_mod_proveedor, form_del_proveedor


urlpatterns = [
    path('', index, name="index"),
    path('dulce', dulce, name="dulce"),
    path('salada', salada, name="salada"),
    path('mixta', mixta, name="mixta"),
    path('contacto', contacto, name="contacto"),
    path('nosotros', nosotros, name="nosotros"),
    path('sismos', sismos, name="sismos"),
    path('home', home, name="home"),
    path('ingreso_proveedor', ingreso_proveedor, name="ingreso_proveedor"),
    path('ingreso_pais', ingreso_pais, name="ingreso_pais"),
    path('listar_proveedor', listar_proveedor, name="listar_proveedor"),
    path('form_mod_proveedor/<id>', form_mod_proveedor, name="form_mod_proveedor"),
    path('form_del_proveedor/<id>', form_del_proveedor, name="form_del_proveedor"),
]