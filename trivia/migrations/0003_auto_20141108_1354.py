# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_question_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=350)),
                ('tags', models.CharField(default=b'empty', max_length=350)),
                ('answer_text', models.CharField(max_length=350)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MCQuestion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=350)),
                ('A', models.CharField(default=b'empty', max_length=100)),
                ('B', models.CharField(default=b'empty', max_length=100)),
                ('C', models.CharField(default=b'empty', max_length=100)),
                ('D', models.CharField(default=b'empty', max_length=100)),
                ('answers', models.CharField(default=b'E', max_length=1, choices=[(b'A', models.CharField(default=b'empty', max_length=100)), (b'B', models.CharField(default=b'empty', max_length=100)), (b'C', models.CharField(default=b'empty', max_length=100)), (b'D', models.CharField(default=b'empty', max_length=100))])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='trivia.MCQuestion'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
