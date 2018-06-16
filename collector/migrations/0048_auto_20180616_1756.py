# Generated by Django 2.0.2 on 2018-06-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0047_auto_20180616_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='role',
            field=models.CharField(choices=[('mastermind', 'Legend'), ('villain', 'Champion'), ('boss', 'Elite'), ('player', 'Veteran'), ('henchman', 'Seasoned'), ('brute', 'Advanced'), ('standard', 'Standard'), ('nameless', 'Nameless')], default='standard', max_length=16),
        ),
    ]
