# Generated by Django 2.2.9 on 2020-04-23 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='status',
            field=models.IntegerField(choices=[(0, 'Ocultar'), (1, 'Publicar')], default=1),
        ),
    ]
