# Generated by Django 4.1 on 2022-09-12 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appuno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='titulo',
            field=models.CharField(max_length=30, verbose_name='Titulo1'),
        ),
    ]