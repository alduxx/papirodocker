# Generated by Django 3.0.7 on 2020-07-29 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0023_auto_20200729_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='parameter_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameter_children', to='descriptor.Parameter'),
        ),
    ]
