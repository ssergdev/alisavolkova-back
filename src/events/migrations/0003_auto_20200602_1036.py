# Generated by Django 3.0.6 on 2020-06-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
        ('events', '0002_auto_20200602_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='artworks',
            field=models.ManyToManyField(blank=True, to='gallery.Artwork'),
        ),
    ]
