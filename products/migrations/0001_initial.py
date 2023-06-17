# Generated by Django 4.2.2 on 2023-06-17 08:41

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('tablas', 'Tablas'), ('ruedas', 'Ruedas'), ('trucks', 'Trucks'), ('lijas', 'Lijas'), ('rulemanes', 'Rulemanes'), ('skate-completo', 'Skate completo'), ('llaves', 'Llaves'), ('remeras', 'Remeras'), ('buzos', 'Buzos'), ('camperas', 'Camperas'), ('gorras', 'Gorras'), ('zapatillas', 'Zapatillas'), ('accesorios', 'Accesorios')], default='tablas', max_length=100)),
                ('image_1', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image_1')),
                ('image_2', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image_2')),
                ('image_3', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image_3')),
                ('size', models.ManyToManyField(blank=True, related_name='products', to='products.size')),
            ],
        ),
    ]