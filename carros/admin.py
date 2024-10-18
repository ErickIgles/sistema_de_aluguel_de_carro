from django.contrib import admin
from .models import Carros
# Register your models here.

@admin.register(Carros)
class CustomCar(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'ano', 'cor', 'quilometragem', 'valor_diario')

