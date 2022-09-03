import datetime

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
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"])
            nickname = request.POST["nickname"]
            area = request.POST["area"]
            profile = Profile(user_id=user.id, nickname=nickname, area=area)
            profile.nickname = nickname
            profile.area = area
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
        username = request.POST['username']
        password = request.POST['password']

        # email is unique,
        user = User.objects.get(username=username)

        if user is None:
            raise AuthenticationFailed('User does not found!')

        # is same?
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        ## JWT 구현 부분
        payload = {
            'id': user.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, "secretJWTkey", algorithm="HS256")

        res = {
            'jwt': token
        }
    return DefaultResponse(200, res)

