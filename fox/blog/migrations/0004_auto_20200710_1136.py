# Generated by Django 3.0.4 on 2020-07-10 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200710_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogview',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 10, 11, 36, 11, 35612)),
        ),
    ]
