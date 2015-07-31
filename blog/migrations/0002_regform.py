# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegForm',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateTimeField(default=django.utils.timezone.now)),
                ('email_id', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('p_address', models.TextField()),
            ],
        ),
    ]
