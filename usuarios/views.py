from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import CustomUserCreateForm, CustomLoginPage, CustomUserChangeForm, PasswordUserChange
from .models import CustomUser
# Create your views here.


def home(request):

    return render(request, 'home.html')


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


def atualizar_usuario(request):

    form = CustomUserChangeForm(instance=request.user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():

            try:
                form.save()
                return redirect('perfil_page')
            except ValueError as err:
                messages.error(request, f'Erro ao atualizar os dados: {err}!')
                return redirect('perfil_page')
    return render(request, 'atualizar_usuario.html', {'form':form})


def atualizar_senha(request):

    form = PasswordUserChange(user=request.user)

    if request.method == 'POST':
        form = PasswordUserChange(user=request.user, data=request.POST)
        
        if form.is_valid():

            try:
                user = form.save()
                update_session_auth_hash(request, user)
                return redirect('perfil_page')
            except ValueError as err:
                messages.error(request, f'Erro ao atualizar a senha {err}')
                return redirect('perfil_page')
    
    return render(request, 'atualizar_senha.html', {'form': form})


def logout_page(request):

    logout(request)
    return redirect('home')


def perfil_page(request):

    user = CustomUser.objects.filter(username=request.user)

    return render(request, 'perfil_page.html', {'user': user})
