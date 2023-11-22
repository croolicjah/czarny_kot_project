# Generated by Django 4.2.7 on 2023-11-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_alter_section_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='state',
            field=models.CharField(blank=True, choices=[('draft', 'nieopublikowany'), ('published', 'opublikowany')], max_length=15, null=True, verbose_name='Stan'),
        ),
    ]
