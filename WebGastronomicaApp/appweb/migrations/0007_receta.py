# Generated by Django 4.2.1 on 2024-04-27 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0006_platos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('ID_Ingrediente_Receta', models.IntegerField(help_text='Id del ingrediente', primary_key=True, serialize=False)),
                ('Cantidad_Ingredientes', models.IntegerField(help_text='Cantidad de ingredientes necesarios')),
                ('ID_Ingrediente_Bodega', models.ForeignKey(help_text='Id del ingrediente en bodega', on_delete=django.db.models.deletion.CASCADE, to='appweb.bodega')),
                ('ID_Plato', models.ForeignKey(help_text='Id del plato', on_delete=django.db.models.deletion.CASCADE, to='appweb.platos')),
            ],
        ),
    ]
