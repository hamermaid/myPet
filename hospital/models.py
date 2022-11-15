from django.db import models


# Create your models here.
# {
#     "hospital_name": "어울림동물병원",
#     "address": "서울 서대문구 남가좌동",
#     "ratings": 4.2,
#     "reviews": 14,
#     "open_hour": "10:00 - 13:00",
#     "restAt": ["일요일"],
#     "labels": ["가좌역", "야간진료", "주간진료"],
#     "is_favorite": true,
#     "now_open": true,
# }
class Hospital(models.Model):
    hos_id = models.CharField(max_length=5, blank=False, unique=True)
    name = models.CharField(max_length=50, blank=False)
    number= models.CharField(max_length=20, blank=True, null=True)
    link = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=2000, blank=True, null=True)
    address = models.CharField(max_length=2000, blank=True, null=True)
    subway = models.CharField(max_length=1000, blank=True, null=True)
    facilitly = models.CharField(max_length=3000, blank=True, null=True)
    animal = models.CharField(max_length=2000, blank=True, null=True)
    clinic = models.CharField(max_length=2000, blank=True, null=True)
    open_time = models.TextField(blank=True, null=True)
    break_time = models.CharField(max_length=2000, blank=True, null=True)
    picture = models.CharField(max_length=2000, blank=True, null=True)
    star = models.CharField(max_length=5, default=0)
