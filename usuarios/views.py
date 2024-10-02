from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreateForm, CustomLoginPage
from .models import CustomUser
# Create your views here.


def home(request):
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
            
            return redirect('home')
        
        else:
            messages.error(request, f'Não foi possível efetuar o cadastro')
    
    return render(request, 'form_usuario.html', {'form': form})


# Sempre tenha uma view function login_page para que os usuários sejam autenticado e apareçam no template.
def login_page(request):

    if request.method == 'POST':
        form = CustomLoginPage(request, data=request.POST)

        if form.is_valid():

            email = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'E-mail ou senha incorreto.')
    else:
        form = CustomLoginPage()
    
    return render(request, 'login_page.html', {'form': form})


def logout_page(request):

    logout(request)
    return redirect('home')
