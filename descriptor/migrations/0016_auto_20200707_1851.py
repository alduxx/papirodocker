# Generated by Django 3.0.7 on 2020-07-07 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0015_auto_20200707_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='parameter_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='descriptor.ParameterGroup'),
        ),
    ]
