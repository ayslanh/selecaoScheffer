# Generated by Django 2.1 on 2018-09-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloAlgodao', '0003_auto_20180908_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoquealgodao',
            name='dtEntrada',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='producao',
            name='dtEntrada',
            field=models.DateTimeField(),
        ),
    ]
