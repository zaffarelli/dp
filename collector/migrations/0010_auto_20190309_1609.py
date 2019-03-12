# Generated by Django 2.1 on 2019-03-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0009_auto_20190309_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='castprofile',
            field=models.ForeignKey(blank=True, default='new castprofile', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.CastProfile'),
        ),
        migrations.AlterField(
            model_name='character',
            name='castrole',
            field=models.ForeignKey(blank=True, default='new castrole', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.CastRole'),
        ),
        migrations.AlterField(
            model_name='character',
            name='castspecies',
            field=models.ForeignKey(blank=True, default='new casteveryman', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.CastEveryman'),
        ),
    ]