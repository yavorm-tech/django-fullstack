# Generated by Django 3.0.7 on 2020-06-30 04:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0009_auto_20200630_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_finnished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 4, 42, 42, 345790, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 4, 42, 42, 345767, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='filemetadata',
            name='file_abs_path',
            field=models.TextField(default='', max_length=64),
        ),
    ]
