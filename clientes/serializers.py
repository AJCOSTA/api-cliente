from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError(
                {'cpf': "O CPF deve ter 11 dígitos"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError(
                {'nome': "Não inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError(
                {'rg': "O RG deve ter 9 dígitos"})

        if not celular_valido(data['celular']):
            """Verifuca se o celular é valido (11 91234-1234)"""
            raise serializers.ValidationError(
                {'celular': "o numero de celular nao é valido "})

        return data
