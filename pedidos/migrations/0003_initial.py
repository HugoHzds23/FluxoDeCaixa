# Generated by Django 4.2 on 2023-05-04 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pedidos', '0002_delete_adicionarpedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='ad_pedido',
            fields=[
                ('origem', models.CharField(choices=[('IFOOD', 'Ifood'), ('BALCAO', 'Balcao'), ('TELEFONE', 'Telefone')], max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('pagamento', models.CharField(choices=[('DINHEIRO', 'Dinheiro'), ('CARTAO DE CREDITO', 'Cartao de Credito'), ('CARTAO DE DEBITO', 'Cartao de Debito'), ('PIX', 'PIX'), ('ONLINE', 'Online')], max_length=100)),
                ('obvervações', models.TextField(blank=True, max_length=200)),
            ],
        ),
    ]
