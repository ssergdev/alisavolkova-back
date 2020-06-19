# Generated by Django 3.0.6 on 2020-06-14 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_auto_20200614_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['ordering', '-created'], 'verbose_name': 'Photo', 'verbose_name_plural': 'Photos'},
        ),
        migrations.AlterModelOptions(
            name='workshop',
            options={'ordering': ['-created'], 'verbose_name': 'Workshop', 'verbose_name_plural': 'Workshops'},
        ),
        migrations.AlterModelOptions(
            name='workshoptranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'Workshop Translation'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='related', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='image',
            field=models.ImageField(upload_to='workshops', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
    ]
