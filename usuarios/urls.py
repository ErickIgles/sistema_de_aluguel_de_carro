
from django.urls import path
from .views import index, criar_usuario, login_page

urlpatterns = [
    path('', index, name='index'),
    path('form_usuario/', criar_usuario, name='criar_usuario'),
    path('login_page/', login_page, name='login_page'),
]