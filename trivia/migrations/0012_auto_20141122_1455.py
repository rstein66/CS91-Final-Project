# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0011_auto_20141122_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcquestion',
            name='answer_text',
            field=models.CharField(default=b'empty', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mcquestion',
            name='answers',
            field=models.CharField(default=b'E', max_length=1, choices=[(b'A', models.CharField(default=b'empty', max_length=100)), (b'B', models.CharField(default=b'empty', max_length=100)), (b'C', models.CharField(default=b'empty', max_length=100)), (b'D', models.CharField(default=b'empty', max_length=100))]),
            preserve_default=True,
        ),
    ]
