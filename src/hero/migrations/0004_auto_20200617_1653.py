# Generated by Django 3.0.6 on 2020-06-17 16:53

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0003_auto_20200614_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerField(blank=True, upload_to='blocks', verbose_name='Image'),
        ),
    ]
