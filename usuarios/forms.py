
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

# Criar usuários junto com senha.
class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser

        labels = {'username':'E-mail'}
        fields = ['email', 'nome', 'sobrenome', 'cpf']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
    

# Editar usuários (exceto senhas)
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        
        fields = ['email', 'nome', 'sobrenome', 'cpf']


class CustomLoginPage(AuthenticationForm):
    username = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
