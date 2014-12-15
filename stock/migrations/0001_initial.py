# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('retail_code', models.CharField(max_length=4)),
                ('material_code', models.CharField(max_length=9)),
                ('description', models.CharField(max_length=21)),
                ('in_stock', models.BooleanField(default=False)),
                ('internal_code', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
