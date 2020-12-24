# Generated by Django 2.2 on 2020-11-11 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0074_auto_20201108_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orbitalitem',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='orbitalitem',
            name='system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.System'),
        ),
    ]