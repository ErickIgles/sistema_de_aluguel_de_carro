from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy
from unittest.mock import patch
from django.contrib import messages
from usuarios.models import CustomUser
from carros.models import AluguelCarro




class AlugandoCarroTestCase(TestCase):

    def setUp(self):

        self.carro = mommy.make('Carros', modelo='Fiesta', imagem='test.png')

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


        self.usuario = CustomUser.objects.create_user(
        email = 'testuser4@gmail.com'
        ,nome = 'Roberto'
        ,sobrenome = 'Carlinhos'
        ,cpf = '12345678915'
        ,password = '123456789@')
        
        self.aluguel = AluguelCarro.objects.create(usuario=self.usuario, carro=self.carro, quantidade_dias=1)


        self.client.login(username=self.dados['email'], password=self.dados['password1'])

    
    def test_alugando_carro(self):

        response = self.client.get(reverse('carros:carro_form', args=[self.carro.id]))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('carros:carro_form', args=[self.carro.id]), data={'confirmar_aluguel':'Confirmar','quantidade_dias': 1})
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('carros:carros_alugados'))
        self.assertContains(response, f'O carro {self.carro.modelo} foi alugado com sucesso.')

    
    @patch('carros.models.AluguelCarro.save')
    def test_alugando_carro_erro(self, mock_save):

        mock_save.side_effect = ValueError('Erro ao alugar')

       
        response = self.client.post(reverse('carros:carro_form', args=[self.carro.id]), data={'quantidade_dias': 1})

        self.assertIn('Erro: Erro ao alugar', [msg.message for msg in messages.get_messages(response.wsgi_request)])
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class CarrosAlugadosTestCase(TestCase):

    def setUp(self):

        self.carro = mommy.make('Carros', modelo='Fiesta', imagem='test.png')

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


        self.usuario = CustomUser.objects.create_user(
        email = 'testuser4@gmail.com'
        ,nome = 'Roberto'
        ,sobrenome = 'Carlinhos'
        ,cpf = '12345678915'
        ,password = '123456789@')
        
        self.aluguel = AluguelCarro.objects.create(usuario=self.usuario, carro=self.carro, quantidade_dias=1)


        self.client.login(username=self.dados['email'], password=self.dados['password1'])

    
    def test_carros_alugados(self):

        response = self.client.get(reverse('carros:carros_alugados'))
        self.assertEqual(response.status_code, 200)



class DevolverCarroTestCase(TestCase):

    def setUp(self):

        self.carro = mommy.make('Carros',modelo='Fiesta', imagem='test.png')

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


        self.usuario = CustomUser.objects.create_user(
        email = 'testuser4@gmail.com'
        ,nome = 'Roberto'
        ,sobrenome = 'Carlinhos'
        ,cpf = '12345678915'
        ,password = '123456789@')
        
        self.aluguel = AluguelCarro.objects.create(usuario=self.usuario, carro=self.carro, quantidade_dias=1)


        self.client.login(username=self.dados['email'], password=self.dados['password1'])
    

    def test_devolver_carro(self):

        response = self.client.get(reverse('carros:devolver_carro', args=[self.aluguel.id]))
        self.assertEqual(response.status_code, 200)
        
        response = self.client.post(reverse('carros:devolver_carro', args=[self.aluguel.id]), data={'devolver_carro': 'Devolver', 'quilometragem_rodada': 100})
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('home'))
        self.assertContains(response, f'O carro {self.carro.modelo} foi devolvido com sucesso.')
        self.assertEqual(response.status_code, 200)

