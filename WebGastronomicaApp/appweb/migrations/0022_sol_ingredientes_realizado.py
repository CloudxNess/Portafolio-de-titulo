# Generated by Django 4.2.1 on 2024-05-14 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0021_alter_platos_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='sol_ingredientes',
            name='Realizado',
            field=models.BooleanField(default=0),
        ),
    ]
