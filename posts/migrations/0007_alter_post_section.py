# Generated by Django 4.2.6 on 2023-10-28 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_section_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='posts.section', verbose_name='Sekcja'),
        ),
    ]
