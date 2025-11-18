from django.db import models
from django.contrib.auth.models import User
import uuid


def generate_unique_code():
    code = uuid.uuid4().hex[:8].upper()
    
    while Homenagem.objects.filter(codigo=code).exists():
        code = uuid.uuid4().hex[:8].upper()
    return code

class Especie(models.Model):
    nome_popular = models.CharField(max_length=100, unique=True)
    nome_cientifico = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Especies' 
        verbose_name = 'Espécie de Árvore'
        verbose_name_plural = 'Espécies de Árvores'

    def __str__(self):
        return self.nome_popular
    
class Homenagem(models.Model):
    codigo = models.CharField(
        max_length=50, 
        unique=True, 
        default=generate_unique_code, 
        blank=True
    )
    nome = models.CharField(max_length=255)
    dataNascimento = models.DateField()
    dataPlantio = models.DateField()
    especie = models.ForeignKey(Especie, on_delete=models.PROTECT, related_name='homenagens')
    
    foto = models.ImageField(upload_to='uploads/')
    
    # NOVOS CAMPOS PARA COORDENADAS
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True) 

    class Meta:
        db_table = 'Homenagens' 

    def __str__(self):
        return self.nome