# Generated by Django 3.0.6 on 2020-06-19 05:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0004_auto_20200617_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidetranslation',
            name='text',
            field=ckeditor.fields.RichTextField(
                blank=True, verbose_name='Text'),
        ),
    ]
