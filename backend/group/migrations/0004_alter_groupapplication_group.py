# Generated by Django 3.2.11 on 2022-02-02 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20220203_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupapplication',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group'),
        ),
    ]