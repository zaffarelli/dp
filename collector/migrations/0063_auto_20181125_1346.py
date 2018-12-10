# Generated by Django 2.0 on 2018-11-25 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0062_auto_20181125_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='act',
            options={'ordering': ['date', 'title']},
        ),
        migrations.AlterModelOptions(
            name='drama',
            options={'ordering': ['epic', 'date', 'title']},
        ),
        migrations.AlterModelOptions(
            name='epic',
            options={'ordering': ['era', 'title']},
        ),
        migrations.AddField(
            model_name='character',
            name='act',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.Act'),
        ),
        migrations.AddField(
            model_name='character',
            name='drama',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.Drama'),
        ),
    ]