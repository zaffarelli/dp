# Generated by Django 2.0.2 on 2018-05-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0021_weaponref_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponref',
            name='damage_class',
            field=models.CharField(blank=True, default='', max_length=16),
        ),
    ]
