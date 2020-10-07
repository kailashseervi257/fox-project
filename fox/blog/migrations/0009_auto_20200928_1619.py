# Generated by Django 3.0.9 on 2020-09-28 10:49

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Mtech', 'Mtech'), ('MBA', 'MBA'), ('UG-Medical', 'UG-Medical'), ('PG-Medical', 'PG-Medical'), ('Engineering', 'Engineering'), ('Commerce', 'Commerce'), ('Law', 'Law'), ('Architecture', 'Architecture'), ('Management', 'Management'), ('All', 'All'), ('Arts', 'Arts')], default='All', max_length=255),
        ),
    ]