# Generated by Django 3.0.6 on 2020-06-12 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workshop',
            options={'ordering': ['-created']},
        ),
    ]
