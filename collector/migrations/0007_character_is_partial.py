# Generated by Django 2.1 on 2019-04-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_character_is_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='is_partial',
            field=models.BooleanField(default=True),
        ),
    ]
