# Generated by Django 2.1 on 2018-12-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scenarist', '0020_auto_20181216_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drama',
            name='title',
            field=models.CharField(blank=True, default='1544998180.5519478', max_length=128, unique=True),
        ),
    ]
