# Generated by Django 4.2 on 2023-05-17 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='novocaixa',
            fields=[
                ('id_caixa', models.AutoField(primary_key=True, serialize=False)),
                ('hora_aberto', models.TimeField(auto_now=True)),
                ('hora_fechado', models.TimeField(auto_now=True)),
            ],
        ),
    ]
