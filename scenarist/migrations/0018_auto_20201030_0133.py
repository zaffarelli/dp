# Generated by Django 2.2 on 2020-10-30 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarist', '0017_auto_20201030_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='full_id',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='drama',
            name='full_id',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='epic',
            name='full_id',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='event',
            name='full_id',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
