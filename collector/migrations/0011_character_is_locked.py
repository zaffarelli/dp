# Generated by Django 2.1 on 2019-03-17 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0010_auto_20190309_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='is_locked',
            field=models.BooleanField(default=False),
        ),
    ]