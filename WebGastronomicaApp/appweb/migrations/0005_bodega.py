# Generated by Django 4.2.1 on 2024-04-27 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0004_ingredientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bodega',
            fields=[
                ('ID_Ing_Bod', models.IntegerField(help_text='Id del ingrediente en la bodega', primary_key=True, serialize=False)),
                ('Cantidad', models.IntegerField(help_text='Cantidad de ingredientes en bodega')),
                ('ID_Ingrediente', models.ForeignKey(help_text='Id del ingrediente', on_delete=django.db.models.deletion.CASCADE, to='appweb.ingredientes')),
            ],
        ),
    ]
