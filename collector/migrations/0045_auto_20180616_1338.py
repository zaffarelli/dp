# Generated by Django 2.0.2 on 2018-06-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0044_character_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='role',
            field=models.CharField(choices=[('mastermind', 'Mastermind'), ('villain', 'Villain'), ('boss', 'Boss'), ('brute', 'Brute'), ('player', 'Player'), ('standard', 'Standard'), ('nameless', 'Nameless')], default='standard', max_length=16),
        ),
    ]