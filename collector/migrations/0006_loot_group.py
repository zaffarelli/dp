# Generated by Django 2.2.7 on 2020-03-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0005_auto_20200320_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='loot',
            name='group',
            field=models.CharField(default='', max_length=128),
        ),
    ]
