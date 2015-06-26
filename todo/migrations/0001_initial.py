# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('taskName', models.CharField(max_length=100)),
                ('taskDescription', models.TextField(default=b'')),
                ('taskDueDate', models.DateField(default=datetime.date.today)),
                ('taskPriority', models.IntegerField(default=3)),
                ('taskStatus', models.CharField(default=b'Todo', max_length=5, choices=[(b'Done', b'Done'), (b'Doing', b'Doing'), (b'Todo', b'Todo')])),
                ('taskOwner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
