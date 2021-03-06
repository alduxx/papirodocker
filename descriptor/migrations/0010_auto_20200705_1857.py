# Generated by Django 3.0.7 on 2020-07-05 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0009_auto_20200703_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='parameter',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='descriptor.Service'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='type',
            field=models.CharField(choices=[('RQ', 'Request'), ('RP', 'Response')], default='RQ', max_length=2, verbose_name='type'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
