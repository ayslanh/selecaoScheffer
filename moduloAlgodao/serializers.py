from .models import Algodao, Beneficiadora, Fazenda, EstoqueAlgodao, Producao
from rest_framework import serializers

class FazendaSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Fazenda
        fields =  '__all__'

class EstoqueAlgodaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueAlgodao
        fields = '__all__'