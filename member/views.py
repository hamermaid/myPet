import datetime
import json

import jwt
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from member.models import Profile
from modual.response import DefaultResponse


def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.nickname = 'test'
    user.save()
    

@csrf_exempt
def signup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if data["password1"] == data["password2"]:
        # if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=data["username"],
                password=data["password1"])
            nickname = data["nickname"]
            # area = data["area"]
            profile = Profile(user_id=user.id, nickname=nickname)
            profile.nickname = nickname
            # profile.area = area
            profile.save()

            auth.login(request, user)
            return DefaultResponse(200, '회원가입 성공')
        return DefaultResponse(200, '회원가입 실패')


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
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return DefaultResponse(400, '잘못된 정보입니다')

        # if user is None:
        #     return DefaultResponse(400, '잘못된 정보입니다')

        # is same?
        if not user.check_password(password):
            return DefaultResponse(400, '잘못된 정보입니다')

        ## JWT 구현 부분
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, "secretJWTkey", algorithm="HS256")

        res = {
            'jwt': token.decode('utf8')
        }
    return DefaultResponse(200, res)

