# Generated by Django 2.1 on 2018-09-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloAlgodao', '0005_auto_20180908_2117'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficiadora',
            options={'ordering': ('idBen',)},
        ),
        migrations.AlterModelOptions(
            name='fazenda',
            options={'ordering': ('idFaz',)},
        ),
        migrations.AlterField(
            model_name='estoquealgodao',
            name='dtEntrada',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='producao',
            name='dtEntrada',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]