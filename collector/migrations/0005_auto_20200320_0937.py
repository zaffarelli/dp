# Generated by Django 2.2.7 on 2020-03-20 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_loot_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loot',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.Character'),
        ),
    ]
