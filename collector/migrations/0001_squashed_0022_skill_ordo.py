# Generated by Django 2.0.2 on 2018-05-05 15:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('collector', '0001_initial'), ('collector', '0002_auto_20180210_2207'), ('collector', '0003_auto_20180210_2212'), ('collector', '0004_character_sa_rec'), ('collector', '0005_auto_20180217_1512'), ('collector', '0006_auto_20180428_1622'), ('collector', '0007_character_rid'), ('collector', '0008_character_pa_total'), ('collector', '0009_auto_20180428_2046'), ('collector', '0010_auto_20180428_2232'), ('collector', '0011_character_narrative'), ('collector', '0012_auto_20180429_2220'), ('collector', '0013_character_age'), ('collector', '0014_auto_20180429_2324'), ('collector', '0015_auto_20180502_0852'), ('collector', '0016_auto_20180502_0852'), ('collector', '0017_character_entrance'), ('collector', '0018_auto_20180505_1131'), ('collector', '0019_auto_20180505_1131'), ('collector', '0020_character_sk_total'), ('collector', '0021_auto_20180505_1232'), ('collector', '0022_skill_ordo')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
                ('PA_AGI', models.IntegerField(default=0)),
                ('PA_AWA', models.IntegerField(default=0)),
                ('PA_BOD', models.IntegerField(default=0)),
                ('PA_CON', models.IntegerField(default=0)),
                ('PA_INT', models.IntegerField(default=0)),
                ('PA_MOV', models.IntegerField(default=0)),
                ('PA_PRE', models.IntegerField(default=0)),
                ('PA_REF', models.IntegerField(default=0)),
                ('PA_STR', models.IntegerField(default=0)),
                ('PA_TEC', models.IntegerField(default=0)),
                ('PA_TEM', models.IntegerField(default=0)),
                ('PA_WIL', models.IntegerField(default=0)),
                ('alliance', models.CharField(default='none', max_length=200)),
                ('player', models.CharField(default='none', max_length=200)),
            ],
        ),
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
                ('is_root', models.BooleanField(default=False)),
                ('is_speciality', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.SkillRef'),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_REC',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_DMG',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_END',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_HUM',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_PAS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_RES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_RUN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_SPD',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_STA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_STU',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_TOL',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='SA_WYR',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date published'),
        ),
        migrations.AddField(
            model_name='character',
            name='rid',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='PA_TOTAL',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='alliance',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_AGI',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_AWA',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_BOD',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_CON',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_INT',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_MOV',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_PRE',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_REF',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_STR',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_TEC',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_TEM',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_WIL',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='character',
            name='narrative',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='character',
            name='birthdate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='caste',
            field=models.CharField(blank=True, default='Freefolk', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.CharField(default='male', max_length=30),
        ),
        migrations.AddField(
            model_name='character',
            name='height',
            field=models.IntegerField(default=150),
        ),
        migrations.AddField(
            model_name='character',
            name='native_fief',
            field=models.CharField(blank=True, default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='rank',
            field=models.CharField(blank=True, default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='species',
            field=models.CharField(default='urthish', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='weight',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='character',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='alliance',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='character',
            name='entrance',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='SK_TOTAL',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_AGI',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_AWA',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_BOD',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_CON',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_INT',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_MOV',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_PRE',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_REF',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_STR',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_TEC',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_TEM',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='character',
            name='PA_WIL',
            field=models.PositiveIntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='skill',
            name='value',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skill',
            name='ordo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
