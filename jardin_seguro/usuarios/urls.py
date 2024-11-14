from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('monitoreo/', views.monitoreo, name='monitoreo'),
    path('ver_camaras/', views.ver_camaras, name='ver_camaras'),
]