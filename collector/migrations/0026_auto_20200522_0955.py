# Generated by Django 2.2.10 on 2020-05-22 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0025_auto_20200522_0954'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ritualref',
            options={'ordering': ['category', 'reference', 'path', 'level'], 'verbose_name': 'References: Ritual'},
        ),
    ]
