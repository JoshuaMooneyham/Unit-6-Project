# Generated by Django 5.0.6 on 2024-06-02 22:05

import django.db.models.deletion
import shortuuid.main
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0016_group_banned_users_userprofile_blocked_users_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="banned_users",
            field=models.ManyToManyField(
                blank=True, related_name="banned_from", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid, max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="blocked_users",
            field=models.ManyToManyField(
                blank=True, related_name="blocked_by", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.CreateModel(
            name="FriendList",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True, related_name="friends", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FriendRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_active", models.BooleanField(blank=True, default=True, null=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="receiver",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sender",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
