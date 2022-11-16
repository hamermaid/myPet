from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=5, blank=True, null=True, unique=True)
    nickname = models.TextField(max_length=500, blank=True)
    likeCnt = models.IntegerField(default=0)
    manner = models.IntegerField(default=0)
    refresh_token = models.TextField(max_length=500, blank=True)
    # area = models.CharField(max_length=30, blank=True)

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()


class Like(models.Model):
    post_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)