# Generated by Django 3.0.4 on 2020-08-03 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_medical_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aviation_form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('TwelfthPercentage', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
