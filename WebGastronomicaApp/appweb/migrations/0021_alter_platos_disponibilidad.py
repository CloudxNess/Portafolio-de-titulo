# Generated by Django 4.2.1 on 2024-05-08 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0020_alter_bodega_id_ing_bod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='Disponibilidad',
            field=models.BooleanField(default=0),
        ),
    ]
