from django.db import models


# Create your models here.

class Reviews(models.Model):
    review_id = models.CharField(max_length=5, blank=False, unique=True)
    hos_id = models.CharField(max_length=5, blank=False)
    user_id = models.CharField(max_length=5, blank=False)
    star = models.CharField(max_length=2000, blank=True, null=True)
    picture = models.CharField(max_length=2000, blank=True, null=True)
    detail = models.CharField(max_length=2000, blank=True, null=True)
    heart = models.CharField(max_length=2000, blank=True, null=True)
    price = models.CharField(max_length=2000, blank=True, null=True)


class Star(models.Model):
    review_id = models.CharField(max_length=5, blank=False, unique=True)
    clinic_id = models.CharField(max_length=5, blank=False)
    star = models.CharField(max_length=5, blank=False)


class Clinic(models.Model):
    clinic_id = models.CharField(max_length=5, blank=False)
    name = models.CharField(max_length=50, blank=False)