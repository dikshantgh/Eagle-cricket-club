# Generated by Django 3.0.5 on 2020-04-26 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricket', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kheladi',
            name='age',
            field=models.PositiveIntegerField(blank=True, max_length=3),
        ),
    ]
