from django.urls import path
from .views import HomenagemListCreate, EspecieList 

urlpatterns = [
    path('homenagens/', HomenagemListCreate.as_view(), name='homenagem-list-create'),
    path('especies/', EspecieList.as_view(), name='especie-list'),
]