# Generated by Django 3.0.5 on 2020-04-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0011_first'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kheladi',
            name='dp',
            field=models.ImageField(default='default_image.jpg', upload_to='profile/', verbose_name='profile picture'),
        ),
    ]
