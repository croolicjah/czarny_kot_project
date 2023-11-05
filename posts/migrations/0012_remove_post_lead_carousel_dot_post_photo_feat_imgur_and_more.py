# Generated by Django 4.2.6 on 2023-11-05 12:17

import czarny_kot.imgur_storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_photo_carousel_imgur_post_photo_feat_imgur_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='lead_carousel_dot',
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_carousel',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Niskie zdjęcie karuzeli (proporcja 1,78; 1973x1110)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_carousel_imgur',
            field=models.ImageField(blank=True, null=True, storage=czarny_kot.imgur_storage.ImgurStorage(), upload_to='CzornyKotPL', verbose_name='Niskie zdjęcie karuzeli (proporcja 1,78; 1973x1110)'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_feat',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Zdjęcie fita (kwadrat)'),
        ),
    ]
