# Generated by Django 2.0.2 on 2018-05-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0005_talent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talent',
            name='description',
            field=models.TextField(blank=True, default='', max_length=512),
        ),
    ]