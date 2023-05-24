# Generated by Django 4.2 on 2023-05-19 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controlecaixa', '0002_alter_novocaixa_hora_fechado'),
    ]

    operations = [
        migrations.AddField(
            model_name='novocaixa',
            name='caixa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='caixa', to=settings.AUTH_USER_MODEL),
        ),
    ]