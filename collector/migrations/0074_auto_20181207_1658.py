# Generated by Django 2.1 on 2018-12-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0073_config_smart_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='narrative',
            field=models.TextField(blank=True, default='', max_length=640),
        ),
        migrations.AlterField(
            model_name='act',
            name='resolution',
            field=models.TextField(blank=True, default='', max_length=640),
        ),
        migrations.AlterField(
            model_name='drama',
            name='description',
            field=models.TextField(blank=True, default='', max_length=640),
        ),
        migrations.AlterField(
            model_name='epic',
            name='description',
            field=models.TextField(blank=True, default='', max_length=640),
        ),
    ]
