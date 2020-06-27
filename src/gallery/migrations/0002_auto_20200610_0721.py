# Generated by Django 3.0.6 on 2020-06-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['ordering', '-created']},
        ),
        migrations.RenameField(
            model_name='photo',
            old_name='artwork',
            new_name='target',
        ),
        migrations.AddField(
            model_name='photo',
            name='ordering',
            field=models.PositiveIntegerField(
                default=0, verbose_name='Ordering'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='related'),
        ),
        migrations.DeleteModel(
            name='PhotoTranslation',
        ),
    ]
