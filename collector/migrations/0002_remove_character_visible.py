# Generated by Django 2.1 on 2019-03-26 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='visible',
        ),
    ]
