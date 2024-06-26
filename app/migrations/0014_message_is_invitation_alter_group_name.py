# Generated by Django 5.0.6 on 2024-06-01 00:49

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0013_group_moderators_alter_group_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="is_invitation",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid, max_length=200
            ),
        ),
    ]
