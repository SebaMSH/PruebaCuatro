from django.core.exceptions import ValidationError
from core.forms import ProveedoresForm, PaisForm
from django.shortcuts import render,redirect
from .models import Proveedores

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def dulce(request):
    return render(request, 'core/dulce.html')

def salada(request):
    return render(request, 'core/salada.html')

def mixta(request):
    return render(request, 'core/mixta.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def sismos(request):
    return render(request, 'core/sismos.html')

def home(request):
    return redirect(to="index")

def ingreso_proveedor(request):
    datos = {
        'form' : ProveedoresForm()
    }

    if request.method == 'POST':
        formulario = ProveedoresForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Proveedor ingresado correctamente"
        else: datos['mensaje'] = "Datos ingresado no validos"
    return render(request, 'core/ingreso_proveedor.html',datos)

def ingreso_pais(request):
    datos = {
        'form' : PaisForm()
    }

    if request.method == 'POST':
        formulario = PaisForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Pais ingresado correctamente"
    return render(request, 'core/ingreso_pais.html',datos)

def listar_proveedor(request):
    Proveedor = Proveedores.objects.all()
    datos = {
        "Proveedor" : Proveedor
    }
    return render(request, 'core/listar_proveedor.html',datos)

def form_del_proveedor(request, id):

    proveedor = Proveedores.objects.get(idProveedor=id)

    proveedor.delete()
    
    return redirect(to="listar_proveedor")

def form_mod_proveedor(request, id):

    proveedor = Proveedores.objects.get(idProveedor=id)

    datos = {
        'form' : ProveedoresForm(instance=proveedor)
    }

    if request.method == 'POST':
        formulariomod = ProveedoresForm(request.POST, instance=proveedor)
        if formulariomod.is_valid:
            formulariomod.save()
            datos['form'] = formulariomod
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/form_mod_proveedor.html', datos)

