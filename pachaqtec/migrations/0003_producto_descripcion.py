# Generated by Django 3.1.3 on 2020-11-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachaqtec', '0002_imagen_producto_plan_estudio_producto_sub_unidad_estudio_unidad_estudio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default='2020-11-26'),
            preserve_default=False,
        ),
    ]