# Generated by Django 5.1.4 on 2025-01-05 23:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_valor', '0004_alter_libro_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'permissions': [('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Owner')], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]