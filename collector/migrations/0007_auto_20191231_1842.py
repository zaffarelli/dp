# Generated by Django 2.2.7 on 2019-12-31 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0006_armorref_tech_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weaponref',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1024),
        ),
    ]