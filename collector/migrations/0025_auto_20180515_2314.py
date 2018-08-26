# Generated by Django 2.0.2 on 2018-05-15 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0024_auto_20180515_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armorref',
            name='reference',
            field=models.CharField(blank=True, default='', max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='shieldref',
            name='reference',
            field=models.CharField(blank=True, default='', max_length=16, unique=True),
        ),
        migrations.AlterField(
            model_name='skillref',
            name='reference',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
