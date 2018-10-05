from django.db import models


'''
Model Fazenda
'''


class Fazenda(models.Model):
    idFaz = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('idFaz',) 

'''
Model Beneficiadora
'''


class Beneficiadora(models.Model):
    idBen = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=45)
    producaoDiaria = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('idBen',) 

'''
Model Algodao 
'''


class Algodao(models.Model):
    idAl = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20)
    peso = models.IntegerField()

    def __str__(self):
        return self.tipo


'''
Model EstoqueAlgodao 
'''


class EstoqueAlgodao(models.Model):
    idEstoque = models.AutoField(primary_key=True)
    fazenda = models.ForeignKey(Fazenda, on_delete=models.CASCADE)
    algodaoTipo = models.ForeignKey(Algodao, on_delete=models.CASCADE)
    dtEntrada = models.DateTimeField(auto_now_add=True)
    qtde = models.IntegerField()

    ''''def __str__(self):
        field_values = []
        for field in self._meta.get_fields():
            field_values.append(str(getattr(self, field.name, '')))
        return ' '.join(field_values)'''
    def __str__(self):
        return f'{self.pk}'

'''
Model Producao
'''


class Producao(models.Model):
    idProd = models.AutoField(primary_key=True)
    dtEntrada = models.DateTimeField(auto_now_add=True)
    beneficiadora = models.ForeignKey(Beneficiadora, on_delete=models.CASCADE)
    estoqueAlgodao = models.ForeignKey(
    EstoqueAlgodao, on_delete=models.CASCADE)
