# Generated by Django 3.1.3 on 2020-11-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachaqtec', '0003_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.CharField(default='2020-11-26', max_length=255),
            preserve_default=False,
        ),
    ]
