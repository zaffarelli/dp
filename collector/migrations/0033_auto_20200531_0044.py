# Generated by Django 2.2.10 on 2020-05-31 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0032_auto_20200531_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficeaffliction',
            name='description',
            field=models.TextField(blank=True, default='', max_length=256, null=True),
        ),
    ]