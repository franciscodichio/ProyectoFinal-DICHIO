from django.contrib import admin

# Register your models here.

from .models import Articulo, Cliente, Operaciones


admin.site.register(Articulo)
admin.site.register(Cliente)
admin.site.register(Operaciones)