# Generated by Django 4.2.1 on 2024-05-06 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0019_alter_bodega_id_ing_bod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodega',
            name='ID_Ing_Bod',
            field=models.AutoField(help_text='Id del ingrediente en la bodega', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingredientes',
            name='ID_Ingrediente',
            field=models.AutoField(help_text='Id del ingrediente', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sol_ingredientes',
            name='ID_Solicitud_Ingrediente',
            field=models.AutoField(help_text='Id de la solicitud', primary_key=True, serialize=False),
        ),
    ]
