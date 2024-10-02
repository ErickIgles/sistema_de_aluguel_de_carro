from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreateForm
# Register your models here.


@admin.register(CustomUser)

class CustomUserAdmin(UserAdmin):

    model = CustomUser

    form = CustomUserChangeForm  # Formulário para edição de usuários 
    add_form = CustomUserCreateForm # Formulário para a criação de usuários.

    list_display = ('email', 'nome', 'sobrenome', 'cpf')


     # Define como os campos do modelo serão organizados na página de edição/adição de usuários na interface administrativa
    
    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Informações Pessoais', {'fields': ('nome', 'sobrenome')}),
        ('Permissões', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined'), 'classes':('collapse',)})
    )
