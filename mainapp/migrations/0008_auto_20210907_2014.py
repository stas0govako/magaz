# Generated by Django 3.2.6 on 2021-09-07 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210907_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antistresstoy',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='plastictoy',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='plushtoy',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]