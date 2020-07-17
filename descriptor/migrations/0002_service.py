# Generated by Django 3.0.7 on 2020-07-01 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('descriptor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('enabled', models.BooleanField(default=True)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='descriptor.Api')),
            ],
        ),
    ]
