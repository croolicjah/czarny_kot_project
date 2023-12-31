# Generated by Django 4.2.6 on 2023-10-27 12:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Nazwa')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Kolejność')),
            ],
            options={
                'verbose_name': 'Sekcja',
                'verbose_name_plural': 'Sekcje',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel_title', models.CharField(max_length=45, verbose_name='Tytuł do karuzeli')),
                ('feat_title', models.CharField(max_length=65, verbose_name='Tytuł do kropki i fit-a')),
                ('photo_carousel', models.ImageField(upload_to='img/', verbose_name='Wąskie zdjęcie do karuzeli')),
                ('photo_feat_dot', models.ImageField(upload_to='img/', verbose_name='Zdjęcie do fita i kropki')),
                ('lead_carousel_dot', models.CharField(max_length=100, verbose_name='Lead do karuzeli i kropki')),
                ('lead_feat', models.CharField(blank=True, max_length=255, null=True, verbose_name='Lead do fit-a')),
                ('content', models.TextField(verbose_name='Treść posta')),
                ('order', models.IntegerField(verbose_name='Miejsce przypięcia')),
                ('publication_date', models.DateField(auto_now_add=True, verbose_name='Data publikacji')),
                ('edit_date', models.DateField(default=django.utils.timezone.now, verbose_name='Data edycji')),
                ('button_text', models.CharField(default='Sprawdź', max_length=25, verbose_name='Napis przycisku')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='posts.section', verbose_name='Sekcja')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posty',
            },
        ),
    ]
