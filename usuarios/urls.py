
from django.urls import path
from .views import home, criar_usuario, login_page, logout_page, perfil_page

urlpatterns = [
    path('', home, name='home'),
    path('form_usuario/', criar_usuario, name='criar_usuario'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('perfil_page/', perfil_page, name='perfil_page'),
]