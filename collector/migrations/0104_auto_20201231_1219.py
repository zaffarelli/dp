# Generated by Django 2.2 on 2020-12-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0103_campaign_back'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='back',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='logo',
        ),
        migrations.AddField(
            model_name='campaign',
            name='black_text',
            field=models.BooleanField(default=True),
        ),
    ]