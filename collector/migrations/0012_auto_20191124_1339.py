# Generated by Django 2.2.7 on 2019-11-24 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0011_auto_20191124_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourofdutyref',
            name='DRK_LVL',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tourofdutyref',
            name='OCC_LVL',
            field=models.IntegerField(default=0),
        ),
    ]
