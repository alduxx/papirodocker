# Generated by Django 3.0.7 on 2020-07-07 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0011_auto_20200707_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametergroup',
            name='parameter',
        ),
        migrations.AddField(
            model_name='parameter',
            name='parameter_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='descriptor.ParameterGroup'),
            preserve_default=False,
        ),
    ]
