# Generated by Django 4.2.3 on 2023-08-29 02:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('practice', '0011_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('privacy', models.CharField(choices=[('PV', 'Private'), ('PB', 'Public'), ('UL', 'Unlisted')], default='PV', max_length=2)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='routines', to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, related_name='routines', to='practice.skill')),
            ],
        ),
        migrations.CreateModel(
            name='RoutineRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='practice.routine')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routine_records', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutineExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routines', to='practice.exercise')),
                ('routine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='practice.routine')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='routine_record',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_records', to='practice.routinerecord'),
        ),
    ]
