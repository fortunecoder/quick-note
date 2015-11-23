# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quicknote', '0003_notebook_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
