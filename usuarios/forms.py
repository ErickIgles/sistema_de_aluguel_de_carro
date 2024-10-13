
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, SetPasswordForm
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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Remove o campo de senha completamente
        if 'password' in self.fields:
            del self.fields['password']
        


class CustomLoginPage(AuthenticationForm):
    username = forms.EmailField(label='E-mail')
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser


class PasswordUserChange(SetPasswordForm):
    new_password1 = forms.CharField(label='Nova senha', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmar Nova Senha', widget=forms.PasswordInput)


    class Meta:
        fields = ['new_password1', 'new_password2']

