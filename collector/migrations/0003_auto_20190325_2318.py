# Generated by Django 2.1 on 2019-03-25 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_auto_20190325_2318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='ready_for_export',
            new_name='is_exportable',
        ),
    ]
