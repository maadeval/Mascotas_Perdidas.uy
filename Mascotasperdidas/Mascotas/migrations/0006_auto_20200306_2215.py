# Generated by Django 3.0.2 on 2020-03-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mascotas', '0005_auto_20200306_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotaperdida',
            name='estado',
            field=models.CharField(max_length=40),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]
