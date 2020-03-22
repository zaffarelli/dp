# Generated by Django 2.2.7 on 2020-03-20 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0008_loot_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='loot',
            name='code',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='loot',
            name='group',
            field=models.CharField(blank=True, default='', max_length=128, null=True),
        ),
    ]
