# Generated by Django 2.0.2 on 2018-08-01 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0054_auto_20180706_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='beneficeafflictionref',
            name='source',
            field=models.CharField(blank=True, default='', max_length=32, null=True),
        ),
    ]