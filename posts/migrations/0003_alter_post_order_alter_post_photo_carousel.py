# Generated by Django 4.2.6 on 2023-10-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_carousel_title_alter_post_feat_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Miejsce przypięcia'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_carousel',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='Wąskie zdjęcie do karuzeli'),
        ),
    ]
