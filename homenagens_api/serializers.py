from rest_framework import serializers
from .models import Homenagem, Especie 

class HomenagemSerializer(serializers.ModelSerializer):
    coordenadas = serializers.SerializerMethodField(read_only=True)
    especie_nome = serializers.CharField(source='especie.nome_popular', read_only=True)

    especie_id = serializers.PrimaryKeyRelatedField(
        queryset=Especie.objects.all(),
        source='especie',
        write_only=True
    )

    class Meta:
        model = Homenagem
        fields = (
            'codigo', 'nome', 'dataNascimento', 'dataPlantio', 
            'especie_nome', 'especie_id', 'foto', 'latitude', 'longitude', 'coordenadas'
        )

    def get_coordenadas(self, obj):
        if obj.latitude is not None and obj.longitude is not None:
            return [obj.latitude, obj.longitude]
        return None
    
    
class EspecieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especie
        fields = ('id', 'nome_popular')