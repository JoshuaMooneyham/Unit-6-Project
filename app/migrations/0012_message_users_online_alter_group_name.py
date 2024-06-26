# Generated by Django 5.0.4 on 2024-05-31 23:41

import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_group_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='users_online',
            field=models.ManyToManyField(blank=True, related_name='online', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=200),
        ),
    ]
