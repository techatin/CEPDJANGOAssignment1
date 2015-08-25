# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('homework', '0003_subject_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='user',
        ),
        migrations.AddField(
            model_name='homework',
            name='user',
            field=models.ForeignKey(blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
