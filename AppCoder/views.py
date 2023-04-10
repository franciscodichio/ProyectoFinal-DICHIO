from django.shortcuts import render
from django.http import HttpResponse

from .models import Articulo
from .models import Cliente
from .models import Operaciones


# Create your views here

 
def inicio(request):
    
    return render(request,"inicio.html")



def articuloFormulario(request):
    
    print('method: ', request.method)
    print('method: ', request.POST)
    
    if request.method == 'POST':
    
        articulo = Articulo(descripcion=request.POST['descripcion'], codigo=request.POST['codigo'], cantidad=request.POST['cantidad'])
        articulo.save()
        
        return render (request, "inicio.html")
         
    return render ( request, "articuloFormulario.html")

def clienteFormulario(request):
    
    print('method: ', request.method)
    print('method: ', request.POST)
    
    if request.method == 'POST':
    
        cliente = Cliente(nom_ape=request.POST['nom_ape'], cuil_t=request.POST['cuil_t'], sit_fis=request.POST['sit_fis'])
        cliente.save()
        
        return render (request, "inicio.html")
        
    return render ( request, "clienteFormulario.html")

def operacionesFormulario(request):
    
    print('method: ', request.method)
    print('method: ', request.POST)
    
    if request.method == 'POST':
    
        operaciones = Operaciones(banco=request.POST['banco'], sucursal=request.POST['sucursal'], cbu=request.POST['cbu'])
        operaciones.save()
        
        return render (request, "inicio.html")
          
    return render ( request, "operacionesFormulario.html")

def articuloLista(request):

    lista = Articulo.objects.all()

    return render(request, "articuloLista.html", {"articuloLista": lista})

def clienteLista(request):

    lista = Cliente.objects.all()

    return render(request, "clienteLista.html", {"clienteLista": lista})

def operacionesLista(request):

    lista = Operaciones.objects.all()

    return render(request, "operacionesLista.html", {"operacionesLista": lista})


def buscarArticulo(request):
         
    return render ( request, "buscarArticulo.html")

def buscar(request):
    
    if request.GET["codigo"]:

        #respuesta = f"Estoy buscando el artículo con código nro: {request.GET['codigo']}"
        
        #return HttpResponse(respuesta)
    
        codigo = request.GET['codigo']
        articulos = Articulo.objects.filter(codigo__icontains=codigo)
        
        return render (request, "resultadosBuscarArticulos.html", {"articulos":articulos, "codigo": codigo})
    
    else:
        respuesta = "No se enviaron datos"
        
    return HttpResponse(respuesta)

def resultadosBuscarArticulos(request):
         
    return render ( request, "resultadosBuscarArticulos.html")