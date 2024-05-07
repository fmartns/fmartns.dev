from django.db import models
from django.contrib.auth.models import User

class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    prefix = models.CharField(max_length=100)
    icon = models.FileField(upload_to='static/icons/')

    def __str__(self):
        return self.name

class UserSocialMedia(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.ForeignKey(SocialMedia, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    position = models.IntegerField(default=0)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100, blank=True)
    is_student = models.BooleanField(default=False)
    primary_color = models.CharField(max_length=7, blank=True)
    secondary_color = models.CharField(max_length=7, blank=True)
    font_color = models.CharField(max_length=7, blank=True)

    def __str__(self):
        return self.user.username
