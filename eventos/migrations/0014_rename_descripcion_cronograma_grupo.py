# Generated by Django 3.2 on 2023-05-17 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0013_alter_evento_mapa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cronograma',
            old_name='descripcion',
            new_name='grupo',
        ),
    ]
