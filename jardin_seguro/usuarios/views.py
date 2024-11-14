from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, MonitoreoCamaraForm
from .models import CamaraMonitoreo

@login_required
def inicio(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    return render(request, 'usuarios/inicio.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario registrado con éxito! Ahora puedes iniciar sesión.')
            return render(request, 'usuarios/registro.html', {'form': form}) 
        else:
            return render(request, 'usuarios/registro.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def monitoreo(request):
    if request.method == 'POST':
        form = MonitoreoCamaraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cámara añadida exitosamente!')
            return redirect('ver_camaras') 
    else:
        form = MonitoreoCamaraForm()
    
    return render(request, 'usuarios/monitoreo.html', {'form': form})

def agregar_camara(request):
    form = MonitoreoCamaraForm()
    form.fields['hora_inicio'].widget.attrs.update({'placeholder': 'HH:MM:SS', 'type': 'time'})
    form.fields['hora_fin'].widget.attrs.update({'placeholder': 'HH:MM:SS', 'type': 'time'})
    
    if request.method == 'POST':
        form = MonitoreoCamaraForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'usuario/ver_camaras.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Has iniciado sesión correctamente.")
            return redirect('inicio') 
        else:
            messages.error(request, "Credenciales incorrectas.")
    else:
        form = AuthenticationForm()

    return render(request, 'usuarios/login.html', {'form': form})

@login_required
def ver_camaras(request):
    cameras = CamaraMonitoreo.objects.all()
    return render(request, 'usuarios/ver_camaras.html', {'cameras': cameras})