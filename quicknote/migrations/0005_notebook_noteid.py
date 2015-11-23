# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quicknote', '0004_auto_20151122_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='noteid',
            field=models.CharField(default=b'B8gNRb5xEDFBkuEKMjaAWM', max_length=200),
        ),
    ]
