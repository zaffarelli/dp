# Generated by Django 2.0.2 on 2018-05-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0032_auto_20180528_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='attributes_list',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='talent',
            name='skills_list',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
