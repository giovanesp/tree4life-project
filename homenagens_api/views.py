from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
from .models import Homenagem, Especie
from .serializers import HomenagemSerializer, EspecieSerializer
from django.db.models import Q

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
    
    
class HomenagemListAPIView(generics.ListAPIView):
    serializer_class = HomenagemSerializer
    pagination_class = StandardResultsPagination 
    
    def get_queryset(self):
        queryset = Homenagem.objects.all()
        params = self.request.query_params

        # 1. Obter os parâmetros da URL
        ne_lat = params.get('ne_lat') 
        ne_lng = params.get('ne_lng') 
        sw_lat = params.get('sw_lat') 
        sw_lng = params.get('sw_lng') 

        if ne_lat and ne_lng and sw_lat and sw_lng:
            try:
                ne_lat = float(ne_lat)
                ne_lng = float(ne_lng)
                sw_lat = float(sw_lat)
                sw_lng = float(sw_lng)
                
                if sw_lng <= ne_lng:
                    # Caso normal (não cruza 180°)
                    queryset = queryset.filter(
                        latitude__gte=sw_lat, 
                        latitude__lte=ne_lat, 
                        longitude__gte=sw_lng, 
                        longitude__lte=ne_lng
                    )
                else:
                    pass 
                
            except ValueError:
                pass

        return queryset