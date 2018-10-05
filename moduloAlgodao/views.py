from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Algodao, Beneficiadora, EstoqueAlgodao, Fazenda, Producao
from .serializers import FazendaSerializer, EstoqueAlgodaoSerializer

class Index(TemplateView):
    template_name = 'index.html'

class gestaoAlgodao(TemplateView):
    template_name = 'gestaoAlgodao.html'

class BuscaFazAPIView(APIView):
    def get(self,request,idFaz):
        #idFaz = request
        fazenda = FazendaSerializer(Fazenda.objects.get(pk=idFaz))
        return Response(fazenda.data)
'''
        Quando a Request for tipo Post vamos criar um novo EstoqueAlgodao.
'''
class Estoque(APIView):
    def post(self,request):
       
        idFaz = request.POST.get("idFazAdd","")
        algodaoTipo = request.POST.get("algodaoTipo", "")
        qtde = request.POST.get("qtde","")
        dtEntrada = request.POST.get('dtEntrada','')
        estoque = EstoqueAlgodao.objects.create(fazenda_id=idFaz,algodaoTipo_id=algodaoTipo,dtEntrada=dtEntrada,qtde=qtde)
        return JsonResponse('{"msg": "Estoque Adiconado com Sucesso!"}',safe=False)

    def get(self,resquest, idFaz):
        estoque = EstoqueAlgodaoSerializer(EstoqueAlgodao.objects.filter(fazenda_id = idFaz),many=True)
        return Response(estoque.data)

