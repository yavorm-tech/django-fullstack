# Generated by Django 3.0.7 on 2020-06-30 04:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20200630_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_finnished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 4, 25, 59, 393360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 4, 25, 59, 393336, tzinfo=utc)),
        ),
    ]
