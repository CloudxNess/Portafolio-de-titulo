# Generated by Django 4.2.1 on 2024-05-01 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0011_remove_usuarios_contraseña_platos_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='Cantidad_Comensales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='platos',
            name='Costo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='platos',
            name='Descripcion',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='platos',
            name='ID_Plato',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='platos',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='platos',
            name='Region',
            field=models.CharField(max_length=50),
        ),
    ]
