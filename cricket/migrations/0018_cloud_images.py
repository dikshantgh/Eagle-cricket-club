# Generated by Django 3.0.5 on 2020-04-29 23:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0017_cloud_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kheladi',
            name='dp',
            field=cloudinary.models.CloudinaryField(db_index=True, max_length=255, verbose_name='profile picture'),
        ),
    ]
