# Generated by Django 3.0.9 on 2020-10-04 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20201004_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuploader',
            name='description',
            field=models.CharField(default='File', max_length=255),
        ),
    ]
