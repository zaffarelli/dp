# Generated by Django 2.0 on 2018-11-24 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0059_epic'),
    ]

    operations = [
        migrations.AddField(
            model_name='act',
            name='epic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.Epic'),
        ),
        migrations.AddField(
            model_name='epic',
            name='gamemaster',
            field=models.CharField(blank=True, default='zaffarelli@gmail.com', max_length=128),
        ),
    ]