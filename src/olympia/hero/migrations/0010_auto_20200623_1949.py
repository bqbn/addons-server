# Generated by Django 2.2.12 on 2020-06-23 19:49

from django.db import migrations, models
import olympia.hero.models


class Migration(migrations.Migration):

    dependencies = [
        ('hero', '0009_auto_20200618_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryheroimage',
            name='custom_image',
            field=models.ImageField(blank=True, upload_to='hero-featured-image/', verbose_name='custom image path'),
        ),
    ]
