# Generated by Django 3.0.6 on 2020-06-08 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, verbose_name='Text'),
        ),
    ]
