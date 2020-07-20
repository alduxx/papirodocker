# Generated by Django 3.0.7 on 2020-07-02 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0006_auto_20200702_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='endpoint_uri',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='endpoint uri'),
        ),
        migrations.AddField(
            model_name='service',
            name='http_method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], default='GET', max_length=6, verbose_name='method'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='api',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='api',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='api',
            name='name',
            field=models.CharField(max_length=60, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='enabled',
            field=models.BooleanField(default=True, verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='service',
            name='iib_service_number',
            field=models.PositiveIntegerField(blank=True, help_text='Insert IIB Service Number if already available. ', null=True, verbose_name='iib service number'),
        ),
        migrations.AlterField(
            model_name='service',
            name='iib_service_version_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='iib service version number'),
        ),
    ]