# Generated by Django 2.1 on 2018-12-09 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0076_auto_20181209_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='act',
            name='foes',
            field=models.TextField(blank=True, default='', max_length=640),
        ),
        migrations.AlterField(
            model_name='act',
            name='friends',
            field=models.TextField(blank=True, default='', max_length=640),
        ),
    ]