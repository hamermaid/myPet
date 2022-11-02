import datetime
import json

import jwt
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from member.models import Profile
from modual.response import DefaultResponse


@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if data["password1"] == data["password2"]:
        # if request.POST["password1"] == request.POST["password2"]:
            # 회원 코드 생성
            u = len(User.objects.all())
            hos_id = str(u + 1) + "3"
            userCode = hos_id.zfill(4)
            # 이메일 중복 검사
            try:
                User.objects.get(email=data["username"])
            except User.DoesNotExist:
                try:
                    user = User.objects.create_user(
                        username=userCode,
                        email=data["username"],
                        password=data["password1"])
                except IntegrityError:
                    return DefaultResponse(400, '잘못된 데이터입니다.')
                nickname = data["nickname"]
                profile = Profile(user_id=userCode, nickname=nickname)
                profile.nickname = nickname
                # profile.area = area
                profile.save()

                auth.login(request, user)
                return DefaultResponse(200, '회원가입에 성공했습니다.')
            return DefaultResponse(400, '중복된 이메일입니다.')
        return DefaultResponse(400, '비밀번호가 일치하지 않습니다.')


# def login(request):
#     if request.method == "GET":
#         authentication = [JSONWebTokenAuthentication]
#         return DefaultResponse(200, '로그인 성공')
#     return DefaultResponse(200, '로그인 실패')


@csrf_exempt
def login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # username = request.POST["username"]
        # password = request.POST["password"]

        username = data["username"]
        password = data["password"]

        # email is unique,
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return DefaultResponse(400, '잘못된 정보입니다')

        # if user is None:
        #     return DefaultResponse(400, '잘못된 정보입니다')

        # is same?
        if not user.check_password(password):
            return DefaultResponse(400, '아이디와 비밀번호가 일치하지 않습니다.')

        ## JWT 구현 부분
        payload = {
            'id': user.username,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, "secretJWTkey", algorithm="HS256")

        res = {
            'jwt': token.decode('utf8')
        }
    return DefaultResponse(200, res)


@csrf_exempt
def email(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data["email"]
        print(email)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return DefaultResponse(200, '사용 가능한 이메일입니다.')

        return DefaultResponse(400, '중복된 이메일입니다.')
