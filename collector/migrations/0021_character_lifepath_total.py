# Generated by Django 2.2.7 on 2019-12-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0020_tourofdutyref_is_custom'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='lifepath_total',
            field=models.IntegerField(default=0),
        ),
    ]
