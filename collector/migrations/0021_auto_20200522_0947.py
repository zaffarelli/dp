# Generated by Django 2.2.10 on 2020-05-22 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0020_auto_20200522_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armorref',
            options={'ordering': ['reference'], 'verbose_name': 'References: Armor'},
        ),
        migrations.AlterModelOptions(
            name='shieldref',
            options={'ordering': ['cost', 'reference'], 'verbose_name': 'References: Shield'},
        ),
        migrations.AlterModelOptions(
            name='weaponref',
            options={'ordering': ['origins', 'reference', 'category', 'damage_class'], 'verbose_name': 'References: Weapon'},
        ),
    ]
