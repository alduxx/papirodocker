# Generated by Django 3.0.7 on 2020-07-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0014_parameter_parameter_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameter',
            name='type',
        ),
        migrations.RemoveField(
            model_name='parametergroup',
            name='label',
        ),
        migrations.AddField(
            model_name='parametergroup',
            name='type',
            field=models.CharField(choices=[('000', 'Requisição'), ('200', 'Response 200 - ok'), ('400', 'Response 400 - error'), ('403', 'Response 403 - forbidden'), ('500', 'Response 500 - server error')], default='000', max_length=3, verbose_name='parameter type'),
            preserve_default=False,
        ),
    ]
