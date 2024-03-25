# Generated by Django 4.1.5 on 2024-03-19 17:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_socialnetwork_userprofile_usersocialnetwork_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="social_networks",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="user",
        ),
        migrations.RemoveField(
            model_name="usersocialnetwork",
            name="social_network",
        ),
        migrations.RemoveField(
            model_name="usersocialnetwork",
            name="user_profile",
        ),
        migrations.DeleteModel(
            name="SocialNetwork",
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
        migrations.DeleteModel(
            name="UserSocialNetwork",
        ),
    ]
