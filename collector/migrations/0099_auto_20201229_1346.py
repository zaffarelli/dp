# Generated by Django 2.2 on 2020-12-29 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0098_auto_20201229_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='rpgsystem',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='rpgsystem',
            name='game_mechanics',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='rpgsystem',
            name='name',
            field=models.CharField(blank=True, default='', max_length=48, unique=True),
        ),
    ]
