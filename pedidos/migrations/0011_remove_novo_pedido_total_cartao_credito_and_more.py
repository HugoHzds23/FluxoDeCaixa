# Generated by Django 4.2 on 2023-05-30 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0010_novo_pedido_total_cartao_credito_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novo_pedido',
            name='total_cartao_credito',
        ),
        migrations.RemoveField(
            model_name='novo_pedido',
            name='total_cartao_debito',
        ),
        migrations.RemoveField(
            model_name='novo_pedido',
            name='total_dinheiro',
        ),
        migrations.RemoveField(
            model_name='novo_pedido',
            name='total_pxi',
        ),
    ]
