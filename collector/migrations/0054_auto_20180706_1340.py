# Generated by Django 2.0.6 on 2018-07-06 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0053_auto_20180706_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficeafflictionref',
            name='description',
            field=models.TextField(blank=True, default='', max_length=256, null=True),
        ),
    ]
