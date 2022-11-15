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
        # hos = Hospital.objects.get(hos_id=req)
        # data = list(hos.values())
        animal = hos.animal.split(',')
        info = hos.facilitly.split(',')
        open = hos.open_time.split('/')
        restAt = []
        openAt = []
        for i in open:
            if '휴무' in i:
                restAt.append(i.replace(' 휴무', '').strip().split(','))
                # restAt = i
            else:
                openAt.append(i.strip())
        # # 토큰에서 userId 찾기
        # user = 'Test00'
        data = {
            "hospital_name": hos.name,      # 병원이름
            "number": hos.number,           # 전화번호
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