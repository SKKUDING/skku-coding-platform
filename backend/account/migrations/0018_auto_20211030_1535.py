# Generated by Django 3.2.4 on 2021-10-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210703_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='session_keys',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='acm_problems_status',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='oi_problems_status',
            field=models.JSONField(default=dict),
        ),
    ]