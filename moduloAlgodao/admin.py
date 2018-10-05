from django.contrib import admin
from .models import Algodao, Beneficiadora, EstoqueAlgodao, Fazenda, Producao
# Register your models here.

admin.site.register(Fazenda)
admin.site.register(Algodao)
admin.site.register(Beneficiadora)
admin.site.register(EstoqueAlgodao)
admin.site.register(Producao)

