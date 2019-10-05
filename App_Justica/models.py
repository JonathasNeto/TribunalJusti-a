from django.db import models

# Create your models here.
from django.db.models import ForeignKey




class Pessoa(models.Model):
    cpf = models.CharField(max_length=12)
    rg = models.CharField(max_length=10)
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    cargo = models.CharField(max_length=20)
    matricula = models.IntegerField()

    def __str__(self):
        return self.cargo

class Documento(models.Model):
    numero = models.IntegerField()
    titulo = models.CharField(max_length=30)
    data = models.DateField()
    texto = models.TextField()
    prazo = models.DateField()

    def __str__(self):
        return self.titulo

class Departamento(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    numero = models.IntegerField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL,null=True)
    interessados = models.ManyToManyField(Pessoa,related_name='Interessados')
    investigados = models.ManyToManyField(Pessoa, related_name='Investigados')
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL,null=True)


class Portaria(Documento):
    proce = models.ForeignKey(Processo, on_delete=models.SET_NULL,null=True)



class Pedido(Documento):
    justificativa = models.TextField()
    maisPra = models.DateField()


class Envio(Documento):
    dataenvio = models.DateField()
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL,null=True)



class Tramitacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.SET_NULL,null=True)
    origem = models.ForeignKey(Departamento, related_name='Origem', on_delete=models.SET_NULL,null=True)
    destino = models.ForeignKey(Departamento, related_name='Destino', on_delete=models.SET_NULL,null=True)
    data = models.DateTimeField()

