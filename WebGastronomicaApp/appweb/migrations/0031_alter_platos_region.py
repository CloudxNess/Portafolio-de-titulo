# Generated by Django 4.2.1 on 2024-06-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0030_alter_platos_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platos',
            name='Region',
            field=models.CharField(choices=[('América del Norte', 'América del Norte'), ('América del Sur', 'América del Sur'), ('Europa', 'Europa'), ('África', 'África'), ('Asia', 'Asia'), ('Oceanía', 'Oceanía')], max_length=50),
        ),
    ]