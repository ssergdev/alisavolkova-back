# Generated by Django 3.0.6 on 2020-06-14 07:44

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0002_auto_20200612_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshoptranslation',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Text'),
        ),
    ]
