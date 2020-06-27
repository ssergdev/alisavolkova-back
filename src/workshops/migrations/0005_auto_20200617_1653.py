# Generated by Django 3.0.6 on 2020-06-17 16:53

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0004_auto_20200614_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerField(
                upload_to='related', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerField(
                upload_to='workshops', verbose_name='Image'),
        ),
    ]
