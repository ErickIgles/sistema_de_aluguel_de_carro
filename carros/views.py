from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Carros, AluguelCarro
from .forms import ReservandoCarro
# Create your views here.


@login_required(login_url='login_page')
def alugando_carro(request, pk):

    if request.method == 'POST':
        form = ReservandoCarro()

        carro = Carros.objects.get(id=pk)
        modelo = carro.modelo
        quantidade_dias = request.POST.get('quantidade_dias')

        try:
            carro_alugado = AluguelCarro(
                usuario = request.user,
                carro = carro,
                quantidade_dias = quantidade_dias

            )
            carro_alugado.save()
            messages.success(request, f'O carro {modelo} foi alugado com sucesso.')
            return redirect('carros:carros_alugados')
        except ValueError as err:
            messages.error(request, f'Erro: {err}')
    else:
        form = ReservandoCarro()

    return render(request, 'carro_form.html', {'form': form})    


@login_required(login_url='login_page')
def carros_alugados(request):
    carro_alugado = AluguelCarro.objects.filter(usuario=request.user)

    return render(request, 'carros_alugados.html', {'carros': carro_alugado})


def devolver_carro(request, pk):
    carro_alugado = AluguelCarro.objects.get(id=pk, usuario=request.user)

    if request.method == 'POST':
        quilometragem_rodada = int(request.POST.get('quilometragem_rodada'))
        carro = carro_alugado.carro
        carro.quilometragem += quilometragem_rodada
        carro.save()


        carro_alugado.delete()
        messages.success(request, f'O carro {carro.modelo} foi devolvido com sucesso.')
        return redirect('carros:carros_alugados')
    
    return render(request, 'carros_alugados.html')

