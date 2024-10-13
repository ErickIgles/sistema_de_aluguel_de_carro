from django.db import models
from stdimage.models import StdImageField
import uuid

from usuarios.models import CustomUser


# Create your models here.

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return filename


class Carros(models.Model):

    placa = models.CharField('Placa do carro', max_length=9)
    marca = models.CharField('Marca do carro', max_length=140)
    modelo = models.CharField('Modelo do carro', max_length=140)
    ano = models.IntegerField('Ano do carro')
    cor = models.CharField('Cor do carro', max_length=140)
    quilometragem = models.IntegerField('Quilometragem do carro')
    valor_diario = models.DecimalField('Valor da diária', max_digits=8, decimal_places=2)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':400, 'height':480, 'crop':True}})


    def __str__(self):
        return f'{self.marca} {self.modelo} {self.ano}'


class AluguelCarro(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carros, on_delete=models.CASCADE)
    quantidade_dias = models.IntegerField(default=1)


    def calcular_valor_aluguel(self):
        return self.quantidade_dias * self.carro.valor_diario
    

    def __str__(self):

        return f'{self.usuario.cpf} {self.carro.marca} {self.carro.modelo} {self.carro.valor_diario}'
 