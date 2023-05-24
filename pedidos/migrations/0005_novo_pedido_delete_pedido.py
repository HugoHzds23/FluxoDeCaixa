# Generated by Django 4.2 on 2023-05-22 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_pedido_delete_ad_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='novo_pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origempedido', models.TextField(choices=[('IFOOD', 'ifood'), ('BALCAO', 'Balcao'), ('TELEFONE', 'Telefone'), ('WHATSAAP', 'WhatSaap')], max_length=50)),
                ('id_ifood', models.CharField(blank=True, max_length=20)),
                ('cliente', models.CharField(max_length=100)),
                ('dinheiro', models.FloatField(blank=True, default='0')),
                ('cartao_debito', models.FloatField(blank=True, default='0')),
                ('pix', models.FloatField(blank=True, default='0')),
                ('cartao_credito', models.FloatField(blank=True, default='0')),
                ('Observacoes', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]