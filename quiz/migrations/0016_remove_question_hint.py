# Generated by Django 2.0.5 on 2019-10-13 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20191012_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='hint',
        ),
    ]
