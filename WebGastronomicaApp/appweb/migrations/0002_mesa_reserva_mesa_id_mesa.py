# Generated by Django 4.2.1 on 2024-04-27 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('ID_Mesa', models.IntegerField(help_text='Id de la mesa', primary_key=True, serialize=False)),
                ('Nombre_Mesa', models.CharField(help_text='Identificador de la mesa', max_length=10)),
                ('Estado_Ocupado', models.BooleanField()),
                ('Estado_Reservado', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='reserva_mesa',
            name='ID_Mesa',
            field=models.ForeignKey(default=0, help_text='Id de la mesa', on_delete=django.db.models.deletion.CASCADE, to='appweb.mesa'),
            preserve_default=False,
        ),
    ]
