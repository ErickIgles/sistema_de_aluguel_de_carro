from django.test import TestCase
from carros.models import get_file_path, AluguelCarro
from usuarios.models import CustomUser
from uuid import uuid4
from model_mommy import mommy

class GetFilePathTestCase(TestCase):


    def setUp(self):

        self.filename = f'{uuid4()}.png'
    

    def test_get_file_path(self):

        self.new_path = get_file_path(None, 'test.png')
        self.assertEqual(len(self.new_path), len(self.filename))


class CarrosTestCase(TestCase):

    def setUp(self):
        self.carro = mommy.make('Carros', marca='ford', modelo='mustang', ano=2014)
    
    def test_str(self):

        esperado = 'ford mustang 2014'
        self.assertEqual(str(self.carro), esperado)


class AluguelCarroTestCase(TestCase):

    def setUp(self):
        self.valor_esperado = 400
        
        self.usuario = mommy.make('CustomUser', cpf='12345678914')
        self.carro = mommy.make('Carros', marca='ford', modelo='mustang', ano=2014, valor_diario=200)
        self.al_carro = AluguelCarro(usuario=self.usuario, carro=self.carro, quantidade_dias=2)


    def test_calcular_valor_aluguel(self):

        valor_resultante = self.al_carro.calcular_valor_aluguel()
        self.assertEqual(valor_resultante, self.valor_esperado)

    
    def test_str(self):
        
        esperado = '12345678914 ford mustang 200'
        self.assertEqual(str(self.al_carro), esperado)
