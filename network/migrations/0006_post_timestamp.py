# Generated by Django 5.0.6 on 2024-10-06 15:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_remove_user_cover_photo_user_followers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
