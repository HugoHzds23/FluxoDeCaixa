# Generated by Django 4.2 on 2023-06-06 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlecaixa', '0001_initial'),
        ('pedidos', '0002_remove_despesa_caixa_remove_pedido_caixa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='despesa',
            name='caixa',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='controlecaixa.caixa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='caixa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='controlecaixa.caixa'),
            preserve_default=False,
        ),
    ]