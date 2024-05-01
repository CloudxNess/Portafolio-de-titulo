# Generated by Django 4.2.1 on 2024-05-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0010_usuarios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='Contraseña',
        ),
        migrations.AddField(
            model_name='platos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='Platos'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Contrasena',
            field=models.CharField(default=0, help_text='Contraseña del usuario', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='Tipo_Usuario',
            field=models.CharField(choices=[('GAR', 'Garzon'), ('COC', 'Cocinero')], default='Garzón', max_length=20),
        ),
    ]
