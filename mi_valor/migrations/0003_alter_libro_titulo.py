# Generated by Django 5.1.4 on 2025-01-05 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_valor', '0002_alter_libro_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]