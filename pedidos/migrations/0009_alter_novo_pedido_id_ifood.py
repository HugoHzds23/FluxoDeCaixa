# Generated by Django 4.2 on 2023-05-22 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_alter_novo_pedido_cartao_credito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novo_pedido',
            name='id_ifood',
            field=models.CharField(blank=True, default=0, max_length=20),
            preserve_default=False,
        ),
    ]
