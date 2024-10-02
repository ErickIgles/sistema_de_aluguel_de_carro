
from django.urls import path
from .views import index, criar_usuario

urlpatterns = [
    path('', index, name='index'),
    path('form_usuario/', criar_usuario, name='criar_usuario'),
]