# Generated by Django 2.0 on 2018-11-25 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0063_auto_20181125_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='act',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.Act'),
        ),
        migrations.AlterField(
            model_name='character',
            name='drama',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.Drama'),
        ),
        migrations.AlterField(
            model_name='character',
            name='epic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.Epic'),
        ),
    ]