# Generated by Django 2.2 on 2021-01-03 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0116_auto_20210103_0139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coc7skillref',
            options={'ordering': ['reference', 'is_root', 'is_speciality', 'is_wildcard'], 'verbose_name': 'COC7: Skill Reference'},
        ),
    ]