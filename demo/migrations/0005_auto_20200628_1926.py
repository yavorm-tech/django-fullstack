# Generated by Django 3.0.7 on 2020-06-28 19:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20200628_0557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_finnished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 19, 26, 12, 526112, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 19, 26, 12, 526088, tzinfo=utc)),
        ),
    ]