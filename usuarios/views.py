from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
            
            login(request, user)
            return redirect('home')
    
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
        form = CustomLoginPage()
    
    return render(request, 'login_page.html', {'form': form})


@login_required(login_url='login_page')
def atualizar_dados(request):

    form = CustomUserChangeForm(instance=request.user)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)

        if form.is_valid():

            form.save()
            messages.info(request, 'Dados atualizados com sucesso!')
            return redirect('perfil_page')

    return render(request, 'atualizar_dados.html', {'form':form})


@login_required(login_url='login_page')
def atualizar_senha(request):

    if request.method == 'POST':
        form = PasswordUserChange(user=request.user, data=request.POST)
        
        if form.is_valid():

            user = form.save()
            update_session_auth_hash(request, user)
            
            messages.info(request, 'Senha atualizada com sucesso!')
            return redirect('perfil_page')
    else:
        form = PasswordUserChange(user=request.user)

    
    return render(request, 'atualizar_senha.html', {'form': form})


@login_required(login_url='login_page')
def deletar_usuario(request):
    
    user = CustomUser.objects.get(username=request.user)

    if request.method == 'POST':
        user.delete()
        
        messages.info(request, 'Conta apagada com sucesso!')

        return redirect('home')
    return render(request, 'deletar_usuario.html')


@login_required(login_url='login_page')
def logout_page(request):

    logout(request)
    return redirect('home')


@login_required(login_url='login_page')
def perfil_page(request):

    user = CustomUser.objects.filter(username=request.user)

    return render(request, 'perfil_page.html', {'user': user})
