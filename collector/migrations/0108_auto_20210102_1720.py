# Generated by Django 2.2 on 2021-01-02 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0107_auto_20201231_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='investigator',
            name='need_fix',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='investigator',
            name='need_pdf',
            field=models.BooleanField(default=False),
        ),
    ]