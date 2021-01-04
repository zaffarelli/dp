# Generated by Django 2.2 on 2020-12-29 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0091_rpgsystem'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='color_back',
            field=models.CharField(default='#00101010', max_length=9),
        ),
        migrations.AddField(
            model_name='config',
            name='color_counterback',
            field=models.CharField(default='#00404040', max_length=9),
        ),
        migrations.AddField(
            model_name='config',
            name='color_front',
            field=models.CharField(default='#00F0F0F0', max_length=9),
        ),
        migrations.AddField(
            model_name='config',
            name='color_linkdown',
            field=models.CharField(default='#00401040', max_length=9),
        ),
        migrations.AddField(
            model_name='config',
            name='color_linkup',
            field=models.CharField(default='#00801080', max_length=9),
        ),
    ]