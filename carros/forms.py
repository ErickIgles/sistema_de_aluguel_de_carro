from django import forms
from django.forms import ModelForm
from .models import AluguelCarro


class ReservandoCarro(ModelForm):

    class Meta:
        model = AluguelCarro
        fields = ['quantidade_dias']

