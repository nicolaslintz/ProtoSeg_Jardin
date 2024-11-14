from django import forms
from .models import Usuario, Camera

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

class MonitoreoCamaraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['nombre', 'ubicacion', 'hora_inicio', 'hora_fin']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre de la cámara'}),
            'ubicacion': forms.TextInput(attrs={'placeholder': 'Ubicación de la cámara'}),
            'hora_inicio': forms.TimeInput(attrs={'placeholder': 'HH:MM:SS', 'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'placeholder': 'HH:MM:SS', 'type': 'time'}),
        }