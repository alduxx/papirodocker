# Generated by Django 3.0.7 on 2020-07-29 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0022_parameter_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='descriptor.Service'),
        ),
    ]
