# Generated by Django 4.1.7 on 2023-11-28 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_carros_remove_pedidos_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carros',
            name='preco',
            field=models.PositiveIntegerField(),
        ),
    ]
