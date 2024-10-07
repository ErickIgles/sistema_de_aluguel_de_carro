from django.test import TestCase
from usuarios.forms import CustomUserCreateForm, CustomUserChangeForm

class CustomUserCreateFormTestCase(TestCase):

    def setUp(self):
        self.email = 'test3user@gmail.com'
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
    
    def test_save_with_commit(self):

        form1 = CustomUserCreateForm(data=self.dados)
        self.assertTrue(form1.is_valid())
        user = form1.save(commit=True)

        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))
    

    def test_save_without_commit(self):

        form1 = CustomUserCreateForm(data=self.dados)
        self.assertTrue(form1.is_valid())
        user = form1.save(commit=False)

        self.assertIsNone(user.id)
        
        # Verifica que os campos foram preenchidos corretamente
        self.assertEqual(user.email, self.dados['email'])
        self.assertEqual(user.nome, self.dados['nome'])
        self.assertEqual(user.sobrenome, self.dados['sobrenome'])
        self.assertEqual(user.cpf, self.dados['cpf'])


class CustomUserChangeFormTestCase(TestCase):

    def setUp(self):
        self.email = 'test3user@gmail.com'
        self.nome = 'Roberto'
        self.sobrenome = 'Carlinhos'
        self.cpf = '12345678915'
        

        self.dados = {
            'username': self.email,
            'email': self.email,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'cpf': self.cpf,
        }    


    def test_remove_password_field(self):
        # Verifica se o campo 'password' não está nos campos do formulário
        form = CustomUserChangeForm(data=self.dados)
        self.assertNotIn('password', form.fields)
    

    def test_form_fields(self):
        # Verifica se os campos necessários estão presentes
        form = CustomUserChangeForm(data=self.dados)
        
        self.assertIn('email', form.fields)
        self.assertIn('nome', form.fields)
        self.assertIn('sobrenome', form.fields)
        self.assertIn('cpf', form.fields)

    
    def test_form_initial_data(self):
        # Verifica se os dados iniciais estão sendo preenchidos corretamente

        form = CustomUserChangeForm(initial=self.dados)

        form.is_valid()
        self.assertEqual(form.initial['email'], self.email)
        self.assertEqual(form.initial['nome'], self.nome)
        self.assertEqual(form.initial['sobrenome'], self.sobrenome)
        self.assertEqual(form.initial['cpf'], self.cpf)

