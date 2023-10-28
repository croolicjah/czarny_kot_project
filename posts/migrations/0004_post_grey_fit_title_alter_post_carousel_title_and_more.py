# Generated by Django 4.2.6 on 2023-10-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_order_alter_post_photo_carousel'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='grey_fit_title',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Szara, 2. część tytułu fit-a'),
        ),
        migrations.AlterField(
            model_name='post',
            name='carousel_title',
            field=models.CharField(max_length=45, verbose_name='Tytuł karuzeli i kropki'),
        ),
        migrations.AlterField(
            model_name='post',
            name='feat_title',
            field=models.CharField(max_length=40, verbose_name='Tytuł fit-a'),
        ),
    ]
