# Generated by Django 3.0.7 on 2020-06-28 20:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20200628_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_finnished',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 20, 26, 17, 509086, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_submitted',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 28, 20, 26, 17, 509060, tzinfo=utc)),
        ),
    ]
