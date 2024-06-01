# Generated by Django 5.0.6 on 2024-06-01 03:06

import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_merge_20240531_2152'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='banned_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='banned_from', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='blocked_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='blocked_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=200),
        ),
    ]
