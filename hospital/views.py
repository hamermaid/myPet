from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from hospital.models import Hospital
from modual.response import DefaultResponse


def list(request):
    if request.method == "GET":
        req = request.GET['id']
        hos = Hospital.objects.get(id=req)
        # data = list(hos.values())
        print('hos', hos)
        keyword = hos.animal_keyword.split(',') + hos.service_keyword.split(',')
        # 토큰에서 userId 찾기
        user = 'Test00'
        # 유저의 즐겨찾기 여부
        favorite = hos.is_favorite.split(',')
        is_favorite = False
        for i in favorite:
            if i == user:
                is_favorite = True
        # 현재 날짜와 오픈 시간 비교해서 오픈 여부 반환
        data = {
            "hospital_name": hos.hospital_name,
            "address": hos.address,
            "ratings": hos.ratings,
            "reviews": hos.reviews,
            "open_hour": hos.open_hour,
            "restAt": hos.restAt,
            "labels": [keyword],
            "is_favorite": is_favorite,
            "now_open": 'true',
          }
    # return DefaultResponse(200, testData)
    return DefaultResponse(200, data)