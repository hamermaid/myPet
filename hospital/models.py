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
    hospital_name = models.CharField(max_length=50, blank=False)
    address = models.TextField(blank=False)
    subway = models.CharField(max_length=50)
    location = models.TextField()
    location2 = models.TextField()
    ratings = models.CharField(max_length=200)
    reviews = models.IntegerField()
    open_hour = models.TextField()
    restAt = models.TextField()
    labels = models.TextField()
    animal_keyword = models.TextField()
    service_keyword = models.TextField()
    is_favorite = models.TextField()
    now_open = models.BooleanField(default=True)
    naver_map = models.URLField()
    website = models.URLField()
    instagram = models.URLField()
    youtube = models.URLField()

