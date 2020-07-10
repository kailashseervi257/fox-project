# Generated by Django 3.0.4 on 2020-07-10 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0009_auto_20200710_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='opening',
            new_name='slug',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
