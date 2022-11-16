from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from hospital.models import Hospital
from modual.response import DefaultResponse
from reviews.models import Reviews


def info(request, hos_id):
    if request.method == "GET":
        try:
            hos = Hospital.objects.get(hos_id=hos_id)
        except Hospital.DoesNotExist:
            return DefaultResponse(400, '잘못된 데이터입니다.')
        review = Reviews.objects.count()    # 해당 병원 리뷰 카운트 가져와야함 - 수정필요
        animal = hos.animal.split(',')
        info = hos.facilitly.split(',')
        open = hos.open_time.split('/')

        # '' 제거
        animal = [v for v in animal if v]
        info = [v for v in info if v]
        open = [v for v in open if v]
        restAt = []
        openAt = []
        for i in open:
            if '휴무' in i:
                # restAt.append(i.replace(' 휴무', '').strip().split(','))
                restAt = i.replace(' 휴무', '').strip().split(',')
                print('restAT', restAt)
            else:
                openAt.append(i.strip())

        number = int(hos.number.replace('-', ''))
        data = {
            "hospital_name": hos.name,      # 병원이름
            "number": number,               # 전화번호
            "page": hos.link,               # 홈페이지
            "address": hos.address,         # 주소
            "subway": hos.subway,           # 지하철역
            "reviews": review,              # 리뷰수
            "open_hour": openAt,            # 오픈 시간
            "restAt": restAt,               # 휴무일
            "lunch_hour": hos.break_time,   # 점심시간
            "ratings": hos.star,            # 별점
            "care_available": animal,       # 케어 동물
            "facilities": info,             # 시설정보
          }
        print('animal', data)
    return DefaultResponse(200, data)