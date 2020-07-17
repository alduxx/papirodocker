# Generated by Django 3.0.7 on 2020-07-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0004_service_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='iib_service_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='iib_service_version_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
