# Generated by Django 2.0.2 on 2018-04-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0012_auto_20180429_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]