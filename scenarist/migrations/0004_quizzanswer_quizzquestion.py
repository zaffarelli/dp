# Generated by Django 2.2 on 2020-10-24 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scenarist', '0003_auto_20200327_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizzQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('num', models.PositiveIntegerField(default=0)),
                ('subject', models.CharField(default='', max_length=64)),
                ('text', models.CharField(blank=True, max_length=128)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='QuizzAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64)),
                ('num', models.PositiveIntegerField(default=0)),
                ('text', models.TextField(default='', max_length=512)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenarist.QuizzQuestion')),
            ],
        ),
    ]
