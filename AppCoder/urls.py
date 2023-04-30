
from django.urls import path
from AppCoder import views


urlpatterns = [   

    path('', views.inicio, name="Inicio"),
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name = 'Register'),
    path('ArticuloFormulario/',views.articuloFormulario, name="ArticuloFormulario"),
    path('ClienteFormulario/',views.clienteFormulario, name="ClienteFormulario"),
    path('OperacionesFormulario/',views.operacionesFormulario, name="OperacionesFormulario"),
    path('ArticuloLista/', views.articuloLista, name="ArticuloLista"),
    path('ClienteLista/', views.clienteLista, name="ClienteLista"),
    path('OperacionesLista/', views.operacionesLista, name="OperacionesLista"),
    path('BuscarArticulo/', views.buscarArticulo, name="BuscarArticulo"),
    path('buscar/', views.buscar, name="buscar"),
    path('ResultadosBuscarArticulos', views.resultadosBuscarArticulos, name="ResultadosBuscarArticulos"),
    
]