# Generated by Django 3.0.5 on 2020-04-29 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0015_cloud_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kheladi',
            name='favourite_cricketer',
            field=models.CharField(max_length=30),
        ),
    ]
