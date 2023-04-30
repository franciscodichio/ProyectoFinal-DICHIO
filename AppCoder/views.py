from django.http import *
from django.shortcuts import render
from django.http import HttpResponse

from .models import Articulo
from .models import Cliente
from .models import Operaciones




def inicio(request) -> HttpResponse:
    return render(request, "inicio.html")


def articuloFormulario(request) -> HttpResponse:
    print('method: ', request.method)
    print('method: ', request.POST)

    if request.method == 'POST':

        articulo = Articulo(
            descripcion=request.POST['descripcion'], codigo=request.POST['codigo'], cantidad=request.POST['cantidad'])
        articulo.save()

        return render(request, "inicio.html")

    return render(request, "articuloFormulario.html")


def clienteFormulario(request) -> HttpResponse:

    print('method: ', request.method)
    print('method: ', request.POST)

    if request.method == 'POST':

        cliente = Cliente(
            nom_ape=request.POST['nom_ape'], cuil_t=request.POST['cuil_t'], sit_fis=request.POST['sit_fis'])
        cliente.save()

        return render(request, "inicio.html")

    return render(request, "clienteFormulario.html")


def operacionesFormulario(request) -> HttpResponse:
    print('method: ', request.method)
    print('method: ', request.POST)

    if request.method == 'POST':

        operaciones = Operaciones(
            banco=request.POST['banco'], sucursal=request.POST['sucursal'], cbu=request.POST['cbu'])
        operaciones.save()

        return render(request, "inicio.html")

    return render(request, "operacionesFormulario.html")


def articuloLista(request) -> HttpResponse:
    lista = Articulo.objects.all()

    return render(request, "articuloLista.html", {"articuloLista": lista})


def clienteLista(request) -> HttpResponse:
    lista = Cliente.objects.all()

    return render(request, "clienteLista.html", {"clienteLista": lista})


def operacionesLista(request) -> HttpResponse:
    lista = Operaciones.objects.all()

    return render(request, "operacionesLista.html", {"operacionesLista": lista})


def buscarArticulo(request) -> HttpResponse:
    return render(request, "buscarArticulo.html")


def buscar(request) -> HttpResponse:
    if request.GET["codigo"]:

        # respuesta = f"Estoy buscando el artículo con código nro: {request.GET['codigo']}"

        # return HttpResponse(respuesta)

        codigo = request.GET['codigo']
        articulos = Articulo.objects.filter(codigo__icontains=codigo)

        return render(request, "resultadosBuscarArticulos.html", {"articulos": articulos, "codigo": codigo})

    else:
        respuesta = "No se enviaron datos"

    return HttpResponse(respuesta)


def resultadosBuscarArticulos(request) -> HttpResponse:
    return render(request, "resultadosBuscarArticulos.html")


def register(request):
    
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario Creado :)"})
        
    else:
        form = UserCreationForm()
        
    return render(request, "AppCoder/registro.html", {"form":form})



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def login_request(request):

    if request .method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():

            usuario = form.cleaned_data.get('username')

            contra = form.cleaned_data.get('password')

            user = authenticate (username=usuario, password=contra)

            
            if user is not None:
                login(request, user)

                return render(request,"AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )

            else:
                return render(request, "Apploder/inicio.html", {"mensaje":"Error, datos incorrectos"} )

        else:
                return render(request,"AppCoder/inicio.html", {"mensaje":"Erorr, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppCoder/login.html", {'form':form} )

