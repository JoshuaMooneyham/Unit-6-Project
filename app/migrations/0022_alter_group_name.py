# Generated by Django 5.0.6 on 2024-06-03 05:30

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_group_name_invitenotification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=200),
        ),
    ]
