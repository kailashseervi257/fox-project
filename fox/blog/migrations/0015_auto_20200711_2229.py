# Generated by Django 3.0.4 on 2020-07-11 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200711_2223'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='blog',
            name='blog_blog_search__46d1ce_gin',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='search_document',
        ),
    ]
