# Generated by Django 3.0.6 on 2020-06-01 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blocks', '0002_auto_20200601_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='slug',
            field=models.SlugField(
                max_length=255, unique=True, verbose_name='Slug'),
        ),
    ]
