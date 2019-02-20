# Generated by Django 2.1 on 2019-02-19 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0003_auto_20190210_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillref',
            name='custom_group',
            field=models.CharField(choices=[('all', 'No group at all'), ('pil', 'Pilot'), ('sci', 'Science'), ('fig', 'Fight')], default='all', max_length=3),
        ),
    ]
