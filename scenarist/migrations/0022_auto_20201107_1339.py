# Generated by Django 2.2 on 2020-11-07 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarist', '0021_auto_20201031_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='chapter',
            field=models.CharField(blank=True, default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='drama',
            name='chapter',
            field=models.CharField(blank=True, default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='epic',
            name='chapter',
            field=models.CharField(blank=True, default='0', max_length=64),
        ),
        migrations.AlterField(
            model_name='event',
            name='chapter',
            field=models.CharField(blank=True, default='0', max_length=64),
        ),
    ]
