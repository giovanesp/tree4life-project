from django.contrib import admin
from .models import Homenagem, Especie

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nome_popular', 'nome_cientifico')
    search_fields = ('nome_popular', 'nome_cientifico')
    fields = ('nome_popular', 'nome_cientifico', 'descricao')
    
@admin.register(Homenagem)
class HomenagemAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'especie', 'dataPlantio', 'latitude', 'longitude')
    search_fields = ('codigo', 'nome')
    list_filter = ('especie__nome_popular', 'dataPlantio') 
    
    readonly_fields = ('codigo',) 

    fields = (
        'codigo', 'nome', 'dataNascimento', 'dataPlantio', 
        'especie', 'foto', 'latitude', 'longitude'
    )