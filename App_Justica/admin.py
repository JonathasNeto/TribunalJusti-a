from django.contrib import admin
from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento,Processo,Pedido,Envio,Tramitacao


admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Processo)
admin.site.register(Pedido)
admin.site.register(Envio)
admin.site.register(Tramitacao)


# Register your models here.
