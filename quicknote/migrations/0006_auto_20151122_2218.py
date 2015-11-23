# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicknote', '0005_notebook_noteid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='noteid',
            field=models.CharField(max_length=200),
        ),
    ]
