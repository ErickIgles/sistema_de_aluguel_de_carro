
from django.urls import path
from .views import home, criar_usuario, login_page, logout_page, perfil_page, atualizar_usuario, atualizar_senha, deletar_usuario

urlpatterns = [
    path('', home, name='home'),
    path('form_usuario/', criar_usuario, name='criar_usuario'),
    path('login_page/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    path('perfil_page/', perfil_page, name='perfil_page'),
    path('atualizar_dados/', atualizar_usuario, name='atualizar_usuario'),
    path('atualizar_senha/', atualizar_senha, name='atualizar_senha'),
    path('deletar_conta/', deletar_usuario, name='deletar_usuario'),
]