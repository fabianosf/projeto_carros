from django.urls import path
from .views import  NewCarCreateView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView


urlpatterns = [   
    path('request/', CarsListView.as_view(), name='cars_request'), # CBV(lista carros e filtra)  
    path('new_car/', NewCarCreateView.as_view(), name='new_car'), # CBV(cria novo carro)
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'), # CBV(detalhe do carro)
    path('car/<int:pk>/update', CarUpdateView.as_view(), name='car_update'), # CBV(update do carro)
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete') # CBV(update do carro)
]