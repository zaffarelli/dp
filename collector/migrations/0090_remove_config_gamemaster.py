# Generated by Django 2.2 on 2020-12-29 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0089_config_gm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config',
            name='gamemaster',
        ),
    ]
