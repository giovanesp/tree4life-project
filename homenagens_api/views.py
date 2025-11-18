from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from .models import Homenagem, Especie
from .serializers import HomenagemSerializer, EspecieSerializer

def home_view(request):
    """Renderiza o arquivo index.html, que contém o mapa Leaflet."""
    return render(request, 'index.html', {})

class StandardResultsPagination(PageNumberPagination):
    page_size_query_param = 'limit' 
    page_size = 1000 


class HomenagemListCreate(generics.ListCreateAPIView):
    queryset = Homenagem.objects.all()
    serializer_class = HomenagemSerializer
    pagination_class = StandardResultsPagination 

    def get_queryset(self):
        queryset = Homenagem.objects.all()
        especie = self.request.query_params.get('especie', None)
        if especie:
            queryset = queryset.filter(especie__nome_popular__iexact=especie)
        return queryset.order_by('-dataPlantio')
    

class EspecieList(generics.ListAPIView):
    queryset = Especie.objects.all().order_by('nome_popular')
    serializer_class = EspecieSerializer