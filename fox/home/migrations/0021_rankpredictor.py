# Generated by Django 3.0.9 on 2021-03-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_popupform'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankPredictor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Exam', models.CharField(blank=True, max_length=50, null=True)),
                ('Score', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]