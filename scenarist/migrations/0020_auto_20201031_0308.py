# Generated by Django 2.2 on 2020-10-31 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenarist', '0019_auto_20201031_0229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizz',
            old_name='framing_event',
            new_name='framingevent',
        ),
    ]