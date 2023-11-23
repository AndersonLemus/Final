from django.shortcuts import render,redirect,get_object_or_404
from .forms import CiudadForm, CustomUserCreationForm
from .models import Ciudad
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def agregar_ciudad(request):
    data = {
        'form': CiudadForm()
    }
    if request.method =='POST':
        formulario = CiudadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            data["mensaje"] = " ciudad agregada correctamente"
        else:
            data["form"] = formulario    
    return render(request,'app/ciudades/agregar.html',data)

def listar_ciudades(request):
    ciudades = Ciudad.objects.all()
    data = {
        'ciudades': ciudades
    }
    return render(request,'app/ciudades/listar.html',data)

def modificar_ciudad(request,id):
    ciudad = get_object_or_404(Ciudad, id=id)
    data = {
        'form':CiudadForm(instance=ciudad)
    }
    if request.method == 'POST':
        formulario = CiudadForm(data=request.POST, instance=ciudad)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_ciudades")
        data["form"] = formulario
    return render(request, 'app/ciudades/modificar.html',data)

def eliminar_ciudad(request,id):
    ciudad = get_object_or_404(Ciudad, id=id)
    ciudad.delete()
    return redirect(to="listar_ciudades")

def registro(request): 
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario =CustomUserCreationForm(data=request.POST)
        if formulario.is_valid(): 
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario 
    return render(request, 'registration/registro.html', data)