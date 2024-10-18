
from django.urls import path
from .views import alugando_carro, carros_alugados, devolver_carro

app_name = 'carros'

urlpatterns = [
    path('carro_form/<int:pk>/', alugando_carro, name='carro_form'),
    path('carros_alugados/', carros_alugados, name='carros_alugados'),
    path('devolver_carro/<int:pk>/', devolver_carro, name='devolver_carro'),
]