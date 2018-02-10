# Generated by Django 2.0.2 on 2018-02-10 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_auto_20180210_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character')),
            ],
        ),
        migrations.CreateModel(
            name='SkillRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='newchar',
            name='identity',
        ),
        migrations.DeleteModel(
            name='NewChar',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.SkillRef'),
        ),
    ]
