"""
URL configuration for GestionInventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from appInventario import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio),
    path('inicioGeneral/', views.inicio),
    path('vistauser/', views.vistaUsuario), 
    path('Sesion/', views.vistaLogin),
    path("registroUsuario/", views.registrarUsuario), 
    path('login/',views.login),
    path('inicioAdmin/', views.inicioAdministrador),
    path("salir/", views.salir),
    path("inicioInstructor/", views.inicioInstructor), 
    path('inicioAsistente/', views.InicioAsistente),
    path('vistaRegistraElemto/', views.vistaRegistrarElementos),
    path('registrarElemento/', views.registrarElementos), 
    path('listarUsuarios/', views.listarUsuarios),
    path('vistaSolicitudes/',views.asistenteSolicitudes),
    path('vistaGestionarElementos/',views.vistaGestionarElementos),
    path('vistaGestionarMateriales/',views.vistaGestionarMateriales),
    path('vistaRegistrarMateriales/',views.vistaRegistrarMateriales),
    path('vistaRegistrarEntradaMaterial/',views.vistaRegistrarEntradaMaterial),
    path('registrarMaterial/',views.registrarMaterial),
    path('registrarEntradaMaterial/',views.registrarEntradaMaterial),
    path('elemento/<str:codigo>', views.getElemento),
    path('elementos/', views.getElementos),
    path('newSolicitud/', views.newSolicitud),
    path('solicitarElementos/',views.SolicitarElementos), 

]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)