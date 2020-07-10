# Generated by Django 3.0.4 on 2020-07-10 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contact_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_request',
            name='requested_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='post_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
