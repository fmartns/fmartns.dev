# Generated by Django 4.1.5 on 2024-03-21 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dashboard", "0004_alter_socialmedia_icon"),
    ]

    operations = [
        migrations.RenameField(
            model_name="socialmedia",
            old_name="socialMedia",
            new_name="name",
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("primary_color", models.CharField(default="#000000", max_length=7)),
                ("secondary_color", models.CharField(default="#FFFFFF", max_length=7)),
                ("visible", models.BooleanField(default=False)),
                (
                    "social_media",
                    models.ManyToManyField(
                        blank=True,
                        related_name="user_profiles",
                        to="dashboard.socialmedia",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
