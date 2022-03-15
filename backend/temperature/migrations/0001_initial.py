# Generated by Django 3.2.10 on 2022-03-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SolvedProblem',
            fields=[
                ('user_id', models.IntegerField(db_index=True)),
                ('id', models.TextField(db_index=True, primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('solved_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'solvedproblem',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(unique=True)),
                ('temeperature', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'temperature',
                'ordering': ('-temeperature',),
            },
        ),
    ]
