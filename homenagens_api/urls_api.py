from django.urls import path
from .views import HomenagemListCreate, HomenagemListAPIView, EspecieList 

urlpatterns = [
    #path('homenagens/', HomenagemListCreate.as_view(), name='homenagem-list-create'),
    path('homenagens/', HomenagemListAPIView.as_view(), name='homenagem-list-filtered'),
    path('especies/', EspecieList.as_view(), name='especie-list'),
]