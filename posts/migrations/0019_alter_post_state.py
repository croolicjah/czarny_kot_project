# Generated by Django 4.2.7 on 2023-11-21 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_post_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(choices=[('draft', 'nieopublikowany'), ('published', 'opublikowany')], default='draft', max_length=15, verbose_name='Stan'),
        ),
    ]
