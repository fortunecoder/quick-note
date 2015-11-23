# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quicknote', '0002_remove_notebook_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
