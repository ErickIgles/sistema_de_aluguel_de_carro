from django.db import models

# Create your models here.
# QUANDO FOR CRIAR UM USUÁRIO CUSTOMIZADO...CRIE O MODELO E DEPOIS CRIE AS MIGRAÇÕES QUE O DJANGO UTILIZA!!!
from django.contrib.auth.models import AbstractUser, BaseUserManager

    
class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email) # realiza a validação se p valor informado é um email verdadeiro.
        user = self.model(email=email, username=email, **extra_fields) 
        user.set_password(password) # criptografa a semha.
        user.save(using=self._db) # salva no banco de dados
        return user # retorna o usuário
    
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False) # o valor "is_superuser" fica recebe o valor False
        return self._create_user(email, password, **extra_fields) # Retorna o usuário não super usuário.
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff must be True')
       
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')
        
        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('first_name', max_length=200)
    last_name = models.CharField('last_name', max_length=200)
    cpf = models.CharField('cpf', max_length=11)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    objects = UserManager()

