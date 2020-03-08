from django.shortcuts import render, redirect
from Mascotas.models import MascotaPerdida
from .forms import MascotaPerdidaForm, MascotaPerdidaForm_e


def home(request):
    mascotas = MascotaPerdida.objects.order_by('-id')                       # <---- mostrar ultimos anuncios al principio
    data = {
        'mascotas':mascotas
    }
    return render(request, 'home.html', data)


def nuevo_ingreso_perdido(request):
    data = {
        'form':MascotaPerdidaForm()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario = MascotaPerdidaForm(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario
       
        if formulario.is_valid():
            formulario.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            data['mensaje'] = "Publicacion Guardada Correctamente"
        data['form'] = formulario                                           # <---- para ingresar las validaciones .forms.py> Alerta_fecha
    return render(request, 'nuevo_ingreso_perdido.html', data)


def nuevo_ingreso_encontrado(request):
    data = {
        'form_e':MascotaPerdidaForm_e()                                         # <---- formulario vacio para rellenar
    }

    if request.method == 'POST':                                            # <---- si enviamos elementos de formulario entra en el 'if'
        formulario_e = MascotaPerdidaForm_e(request.POST, files=request.FILES)  # <---- metemos los elementos en el formulario

        if formulario_e.is_valid():
            formulario_e.save()                                               # <---- si se validan los datos, se guarda y se envia al servidor
            data['mensaje'] = "Publicacion Guardada Correctamente"
        data['form_e'] = formulario_e
    return render(request, 'nuevo_ingreso_encontrado.html', data)


def Listado_publicaciones(request):
    listado = MascotaPerdida.objects.all()
    data = {
        'listado': listado
    }
    return render(request, 'listado_publicaciones.html', data)


def Modificar_publicaciones(request, id):
    modificar = MascotaPerdida.objects.get(id=id)
    data = {
        'form': MascotaPerdidaForm(instance=modificar)
    }

    if request.method == 'POST':
        formulario = MascotaPerdidaForm(data=request.POST, files=request.FILES, instance=modificar)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificacion realizada correctamente"
            data['form'] = formulario

    return render(request, 'modificar_publicaciones.html', data)


def Eliminar_publicacion(request, id):
    publicacion = MascotaPerdida.objects.get(id=id)
    publicacion.delete()

    return redirect(to="listado_publicaciones")