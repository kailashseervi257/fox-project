# Generated by Django 3.0.9 on 2021-03-11 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('url', models.CharField(default=None, max_length=255)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('body', models.TextField(blank=True)),
                ('views_total', models.IntegerField(default=1)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('Mtech', 'Mtech'), ('MBA', 'MBA'), ('UG-Medical', 'UG-Medical'), ('PG-Medical', 'PG-Medical'), ('Engineering', 'Engineering'), ('Commerce', 'Commerce'), ('Law', 'Law'), ('Architecture', 'Architecture'), ('Management', 'Management'), ('All', 'All'), ('Arts', 'Arts'), ('Updates', 'Updates')], default='All', max_length=255)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='FileUploader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/')),
                ('description', models.CharField(default='File', max_length=255)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderBlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blog')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='BlogView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('session', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='BlogImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('blog', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]
