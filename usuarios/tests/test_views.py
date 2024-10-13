from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password

from usuarios.forms import CustomUserCreateForm


class CriarUsuarioTestCase(TestCase):

    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@' 

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }

    
    def test_criar_usuario_view(self):
        response = self.client.post(reverse('criar_usuario'), data=self.dados)

        # Verifica se a resposta redireciona corretamente
        self.assertEqual(response.status_code, 302)  # Verifica se foi redirecionado
        self.assertRedirects(response, reverse('home'))  # Verifica se redirecionou para a página correta

        # Verifica se o usuário foi realmente criado
        User = get_user_model()  # Obtém o modelo de usuário atual
        user = User.objects.get(email=self.email)

        self.assertIsNotNone(user)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
    

    def test_criar_usuario_invalido(self):
        self.dados2 = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
             # 'password1' e 'password2' estão ausentes intencionalmente
        }
        
        response = self.client.post(reverse('criar_usuario'), data=self.dados2)

        
        self.assertEqual(response.status_code, 200) 

    
class LoginPageTestCase(TestCase):

    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@' 

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }

    
    def test_login_page(self):
        self.client.post(reverse('criar_usuario'), data=self.dados)
        
        self.dados2 = {
            'username': self.email,
            'password': self.password
        }

        response = self.client.post(reverse('login_page'), data=self.dados2)
        
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(self.client.login(username=self.email, password=self.password))
    

    def test_login_page_get(self):
        self.client.get(reverse('login_page'))


class LogoutPageTestCase(TestCase):

    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@' 

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }


    def test_logout_page(self):

        self.client.post(reverse('criar_usuario'), data=self.dados)

        login_required = self.client.login(username=self.email, password=self.password)
        self.assertTrue(login_required)

        response = self.client.get(reverse('logout_page'))
        self.assertEqual(response.status_code, 302)


class PerfilPageTestCase(TestCase):

    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@' 

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }

    
    def test_perfil_page(self):

        self.client.post(reverse('criar_usuario'), data=self.dados)

        login_required = self.client.login(username=self.email, password=self.password)
        self.assertTrue(login_required)

        response = self.client.get(reverse('perfil_page'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.email)        


class AtualizarDadosTestCase(TestCase):
    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@' 

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }

    
    def test_atualizar_dados(self):

        dados_atualizados = {
            'username': 'novoemail@gmail.com',
            'email': 'novoemail@gmail.com',
            'nome': 'Roberto Atualizado',
            'sobrenome': 'Carlinhos Atualizado',
            'cpf': '12345678915',  # CPF permanece o mesmo
        }

        self.client.post(reverse('criar_usuario'), data=self.dados)

        response = self.client.get(reverse('atualizar_dados'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('atualizar_dados'), data=dados_atualizados)

        response = self.client.post(reverse('atualizar_dados'), data={'atualizar_dados': 'Atualizar'})
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get(reverse('perfil_page'))
        self.assertContains(response, 'Dados atualizados com sucesso!')

        User = get_user_model()  # Obtém o modelo de usuário atual
        user = User.objects.get(username=self.email)

        self.assertEqual(str(user), dados_atualizados['email'])
        self.assertEqual(user.email, dados_atualizados['email'])
        self.assertEqual(user.nome, dados_atualizados['nome'])
        self.assertEqual(user.sobrenome, dados_atualizados['sobrenome'])
        self.assertEqual(user.cpf, dados_atualizados['cpf'])


from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AtualizarSenhaTestCase(TestCase):
    
    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@'

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }

    def test_atualizar_senha(self):
        # Primeiro, crie o usuário
        self.client.post(reverse('criar_usuario'), data=self.dados)

        # Acesse a página de atualização de senha
        response = self.client.get(reverse('atualizar_senha'))
        self.assertEqual(response.status_code, 200)

        # Nova senha
        self.new_password = '741852963@'
        senha_atualizada = {
            'password1': self.new_password,
            'password2': self.new_password
        }

        # Atualize a senha
        response = self.client.post(reverse('atualizar_senha'), data={'new_password1': senha_atualizada['password1'], 'new_password2': senha_atualizada['password2']})
        self.assertEqual(response.status_code, 302)

        # Verifique a mensagem de sucesso na página de perfil
        response = self.client.get(reverse('perfil_page'))

        self.assertContains(response, 'Senha atualizada com sucesso!')
        User = get_user_model()
        user = User.objects.get(username=self.email)

        self.assertTrue(user.check_password(self.new_password))


class DeletarUsuarioTestCase(TestCase):

    def setUp(self):
        self.email = 'testuser4@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        self.password = '123456789@' 

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
            'password1': self.password,
            'password2': self.password
        }
    
    def test_deletar_usuario(self):

        self.client.post(reverse('criar_usuario'), data=self.dados)

        response = self.client.get(reverse('deletar_usuario'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('deletar_usuario'), data={'confirmar': 'Continuar'})        
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Conta apagada com sucesso!')
