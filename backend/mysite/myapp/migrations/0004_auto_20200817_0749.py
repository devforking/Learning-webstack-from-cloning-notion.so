# Generated by Django 3.1 on 2020-08-17 07:49

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200817_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elements',
            name='style',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]