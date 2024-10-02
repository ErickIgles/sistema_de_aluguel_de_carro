from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreateForm
from .models import CustomUser
# Create your views here.


def index(request):
    usuarios = CustomUser.objects.all()

    return render(request, 'home.html', {'usuarios': usuarios})


def criar_usuario(request):
    
    form = CustomUserCreateForm()

    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.username = user.email.lower()
            user.save()

            messages.success(request, f'Seja bem-vindo, {user.nome}')
            
            return redirect('index')
        
        else:
            messages.error(request, f'Não foi possível efetuar o cadastro')
    
    return render(request, 'form_usuario.html', {'form': form})



