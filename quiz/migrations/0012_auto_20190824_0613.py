# Generated by Django 2.1.4 on 2019-08-24 06:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20190824_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='submit_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 24, 6, 13, 43, 549032, tzinfo=utc)),
        ),
    ]
