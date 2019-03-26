# Generated by Django 2.1 on 2019-03-25 23:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scenarist', '0030_auto_20190310_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ArmorRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, default='', max_length=64, unique=True)),
                ('category', models.CharField(blank=True, choices=[('Soft', 'Soft Armor'), ('Medium', 'Medium Armor'), ('Hard', 'Hard Armor')], default='Soft', max_length=6)),
                ('head', models.BooleanField(default=False)),
                ('torso', models.BooleanField(default=True)),
                ('left_arm', models.BooleanField(default=True)),
                ('right_arm', models.BooleanField(default=True)),
                ('left_leg', models.BooleanField(default=False)),
                ('right_leg', models.BooleanField(default=False)),
                ('stopping_power', models.PositiveIntegerField(blank=True, default=2)),
                ('cost', models.PositiveIntegerField(blank=True, default=2)),
                ('encumbrance', models.PositiveIntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True, default='', max_length=128)),
            ],
            options={
                'ordering': ['reference'],
            },
        ),
        migrations.CreateModel(
            name='BeneficeAffliction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='', max_length=256, null=True)),
            ],
            options={
                'ordering': ['beneficeaffliction_ref'],
            },
        ),
        migrations.CreateModel(
            name='BeneficeAfflictionRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=64)),
                ('value', models.IntegerField(default=0)),
                ('category', models.CharField(choices=[('ba', 'Background'), ('co', 'Community'), ('po', 'Possessions'), ('ri', 'Riches'), ('st', 'Status'), ('ot', 'Other')], default='ot', max_length=2)),
                ('description', models.TextField(blank=True, default='', max_length=256, null=True)),
                ('source', models.CharField(blank=True, default='', max_length=32, null=True)),
            ],
            options={
                'ordering': ['reference'],
            },
        ),
        migrations.CreateModel(
            name='BlessingCurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('description', models.TextField(blank=True, default='', max_length=128)),
                ('value', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CastEveryman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(blank=True, default='', max_length=64)),
                ('race', models.CharField(blank=True, default='', max_length=64)),
                ('racial_attr_mod', models.CharField(default='{}', max_length=128)),
                ('racial_skills', models.CharField(default='{}', max_length=512)),
                ('racial_occult', models.CharField(default='{}', max_length=128)),
                ('attr_mod_balance', models.IntegerField(default=0)),
                ('skill_balance', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, default='', max_length=512)),
            ],
            options={
                'ordering': ['species', 'race'],
            },
        ),
        migrations.CreateModel(
            name='CastProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, default='new_profile', max_length=64, unique=True)),
                ('weights', models.CharField(default='[1,1,1,1,1,1,1,1,1,1,1,1]', max_length=128)),
                ('groups', models.CharField(default='[]', max_length=128)),
            ],
            options={
                'ordering': ['reference'],
            },
        ),
        migrations.CreateModel(
            name='CastRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, default='new_role', max_length=64, unique=True)),
                ('value', models.PositiveIntegerField(default=0)),
                ('primaries', models.PositiveIntegerField(default=0)),
                ('maxi', models.PositiveIntegerField(default=10)),
                ('mini', models.PositiveIntegerField(default=1)),
                ('skills', models.PositiveIntegerField(default=0)),
                ('talents', models.PositiveIntegerField(default=0)),
                ('ba', models.PositiveIntegerField(default=0)),
                ('bc', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['reference'],
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('rid', models.CharField(default='none', max_length=200)),
                ('alliance', models.CharField(blank=True, default='', max_length=200)),
                ('alliancehash', models.CharField(blank=True, default='none', max_length=200)),
                ('player', models.CharField(blank=True, default='', max_length=200)),
                ('birthdate', models.IntegerField(default=0)),
                ('gender', models.CharField(default='female', max_length=30)),
                ('native_fief', models.CharField(blank=True, default='none', max_length=200)),
                ('caste', models.CharField(blank=True, default='Freefolk', max_length=100)),
                ('rank', models.CharField(blank=True, default='', max_length=100)),
                ('height', models.IntegerField(default=150)),
                ('weight', models.IntegerField(default=50)),
                ('narrative', models.TextField(blank=True, default='')),
                ('entrance', models.CharField(blank=True, default='', max_length=100)),
                ('keyword', models.CharField(blank=True, default='', max_length=32)),
                ('stars', models.CharField(blank=True, default='', max_length=256)),
                ('PA_STR', models.PositiveIntegerField(default=3)),
                ('PA_CON', models.PositiveIntegerField(default=3)),
                ('PA_BOD', models.PositiveIntegerField(default=3)),
                ('PA_MOV', models.PositiveIntegerField(default=3)),
                ('PA_INT', models.PositiveIntegerField(default=3)),
                ('PA_WIL', models.PositiveIntegerField(default=3)),
                ('PA_TEM', models.PositiveIntegerField(default=3)),
                ('PA_PRE', models.PositiveIntegerField(default=3)),
                ('PA_REF', models.PositiveIntegerField(default=3)),
                ('PA_TEC', models.PositiveIntegerField(default=3)),
                ('PA_AGI', models.PositiveIntegerField(default=3)),
                ('PA_AWA', models.PositiveIntegerField(default=3)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date published')),
                ('SA_REC', models.IntegerField(default=0)),
                ('SA_STA', models.IntegerField(default=0)),
                ('SA_END', models.IntegerField(default=0)),
                ('SA_STU', models.IntegerField(default=0)),
                ('SA_RES', models.IntegerField(default=0)),
                ('SA_DMG', models.IntegerField(default=0)),
                ('SA_TOL', models.IntegerField(default=0)),
                ('SA_HUM', models.IntegerField(default=0)),
                ('SA_PAS', models.IntegerField(default=0)),
                ('SA_WYR', models.IntegerField(default=0)),
                ('SA_SPD', models.IntegerField(default=0)),
                ('SA_RUN', models.IntegerField(default=0)),
                ('PA_TOTAL', models.IntegerField(default=0)),
                ('SK_TOTAL', models.IntegerField(default=0)),
                ('TA_TOTAL', models.IntegerField(default=0)),
                ('BC_TOTAL', models.IntegerField(default=0)),
                ('BA_TOTAL', models.IntegerField(default=0)),
                ('weapon_cost', models.IntegerField(default=0)),
                ('armor_cost', models.IntegerField(default=0)),
                ('shield_cost', models.IntegerField(default=0)),
                ('AP', models.IntegerField(default=0)),
                ('OP', models.IntegerField(default=0)),
                ('gm_shortcuts', models.TextField(blank=True, default='')),
                ('age', models.IntegerField(default=0)),
                ('occult_level', models.PositiveIntegerField(default=0)),
                ('occult_darkside', models.PositiveIntegerField(default=0)),
                ('occult', models.CharField(blank=True, default='', max_length=50)),
                ('challenge', models.TextField(blank=True, default='')),
                ('is_exportable', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_dead', models.BooleanField(default=False)),
                ('is_locked', models.BooleanField(default=False)),
                ('onsave_reroll_attributes', models.BooleanField(default=False)),
                ('onsave_reroll_skills', models.BooleanField(default=False)),
                ('build_log', models.TextField(blank=True, default='')),
                ('castprofile', models.ForeignKey(blank=True, default='new castprofile', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.CastProfile')),
                ('castrole', models.ForeignKey(blank=True, default='new castrole', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.CastRole')),
                ('castspecies', models.ForeignKey(blank=True, default='new casteveryman', null=True, on_delete=django.db.models.deletion.SET_NULL, to='collector.CastEveryman')),
                ('epic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scenarist.Epic')),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=128, unique=True)),
                ('description', models.TextField(blank=True, default='', max_length=128)),
                ('gamemaster', models.CharField(blank=True, default='zaffarelli@gmail.com', max_length=128)),
                ('is_active', models.BooleanField(default=False)),
                ('smart_code', models.CharField(blank=True, default='xxxxxx', max_length=6)),
                ('current_drama', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scenarist.Drama')),
                ('epic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scenarist.Epic')),
            ],
            options={
                'ordering': ['title', 'epic'],
            },
        ),
        migrations.CreateModel(
            name='Shield',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charges', models.PositiveIntegerField(blank=True, default=10)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character')),
            ],
        ),
        migrations.CreateModel(
            name='ShieldRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, default='', max_length=16, unique=True)),
                ('protection_min', models.PositiveIntegerField(blank=True, default=10)),
                ('protection_max', models.PositiveIntegerField(blank=True, default=20)),
                ('hits', models.PositiveIntegerField(blank=True, default=10)),
                ('cost', models.PositiveIntegerField(blank=True, default=500)),
                ('is_compatible_with_medium_armor', models.BooleanField(default=False)),
                ('is_compatible_with_hard_armor', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='', max_length=128)),
            ],
            options={
                'ordering': ['reference'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character')),
            ],
            options={
                'ordering': ['skill_ref'],
            },
        ),
        migrations.CreateModel(
            name='SkillRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=200, unique=True)),
                ('is_root', models.BooleanField(default=False)),
                ('is_speciality', models.BooleanField(default=False)),
                ('group', models.CharField(choices=[('AWA', 'Awareness'), ('BOD', 'Physical'), ('CON', 'Control'), ('DIP', 'Diplomacy'), ('EDU', 'Education'), ('FIG', 'Combat'), ('PER', 'Performance'), ('SOC', 'Social'), ('SPI', 'Spirituality'), ('TIN', 'Tinkering'), ('UND', 'Underworld')], default='EDU', max_length=3)),
                ('linked_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collector.SkillRef')),
            ],
            options={
                'ordering': ['is_speciality', 'reference'],
            },
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('attributes_list', models.CharField(blank=True, default='', max_length=128)),
                ('skills_list', models.CharField(blank=True, default='', max_length=128)),
                ('description', models.TextField(blank=True, default='', max_length=1024)),
                ('AP', models.IntegerField(default=0)),
                ('OP', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammoes', models.PositiveIntegerField(blank=True, default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponRef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, default='', max_length=64, unique=True)),
                ('category', models.CharField(blank=True, choices=[('MELEE', 'Melee weapon'), ('P', 'Pistol/revolver'), ('RIF', 'Rifle'), ('SMG', 'Submachinegun'), ('SHG', 'Shotgun'), ('HVY', 'Heavy weapon'), ('EX', 'Exotic weapon')], default='RIF', max_length=5)),
                ('weapon_accuracy', models.IntegerField(blank=True, default=0)),
                ('conceilable', models.CharField(blank=True, choices=[('P', 'Pocket'), ('J', 'Jacket'), ('L', 'Long coat'), ('N', "Can't be hidden")], default='J', max_length=1)),
                ('availability', models.CharField(blank=True, choices=[('E', 'Excellent'), ('C', 'Common'), ('P', 'Poor'), ('R', 'Rare')], default='C', max_length=1)),
                ('damage_class', models.CharField(blank=True, default='', max_length=16)),
                ('caliber', models.CharField(blank=True, default='', max_length=16)),
                ('str_min', models.PositiveIntegerField(blank=True, default=0)),
                ('rof', models.PositiveIntegerField(blank=True, default=0)),
                ('clip', models.PositiveIntegerField(blank=True, default=0)),
                ('rng', models.PositiveIntegerField(blank=True, default=0)),
                ('rel', models.CharField(blank=True, choices=[('VR', 'Very reliable'), ('ST', 'Standard'), ('UR', 'Unreliable')], default='ST', max_length=2)),
                ('cost', models.PositiveIntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True, default='', max_length=256)),
                ('stats', models.CharField(blank=True, default='', max_length=256)),
                ('origins', models.CharField(blank=True, default='', max_length=64)),
            ],
            options={
                'ordering': ['reference', 'category', 'damage_class'],
            },
        ),
        migrations.AddField(
            model_name='weapon',
            name='weapon_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.WeaponRef'),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.SkillRef'),
        ),
        migrations.AddField(
            model_name='shield',
            name='shield_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.ShieldRef'),
        ),
        migrations.AlterUniqueTogether(
            name='casteveryman',
            unique_together={('species', 'race')},
        ),
        migrations.AddField(
            model_name='blessingcurse',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character'),
        ),
        migrations.AddField(
            model_name='beneficeaffliction',
            name='beneficeaffliction_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.BeneficeAfflictionRef'),
        ),
        migrations.AddField(
            model_name='beneficeaffliction',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character'),
        ),
        migrations.AddField(
            model_name='armor',
            name='armor_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.ArmorRef'),
        ),
        migrations.AddField(
            model_name='armor',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collector.Character'),
        ),
    ]
