# Generated by Django 2.1 on 2019-03-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0007_casteveryman_skill_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casteveryman',
            name='species',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]