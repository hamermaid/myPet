import datetime
import json

import jwt
from django.contrib import auth
from django.contrib.auth.models import User
from django.db import IntegrityError
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from member.models import Profile
from modual.response import DefaultResponse
from myPet.settings import SECRET_KEY


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

        # is same?
        if not user.check_password(password):
            return DefaultResponse(400, '아이디와 비밀번호가 일치하지 않습니다.')

        ## JWT 구현 부분
        access = {
            'id': user.username,
            'exp': (datetime.datetime.now() + datetime.timedelta(minutes=60)).strftime("%Y%m%d%H%M%S"),
            'iat': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "token_type": "access",
        }
        refresh = {
            'id': user.username,
            'exp': (datetime.datetime.now() + datetime.timedelta(minutes=120)).strftime("%Y%m%d%H%M%S"),
            'iat': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
            "token_type": "refresh",
        }

        acc_token = jwt.encode(access, SECRET_KEY, algorithm="HS256").decode('utf8')
        re_token = jwt.encode(refresh, SECRET_KEY, algorithm="HS256").decode('utf8')

        profile = Profile.objects.get(user_id=user.username)
        profile.refresh_token = re_token
        profile.save()

        res = {
            'access': acc_token,
            'refresh': re_token
        }
    return DefaultResponse(200, res)


@csrf_exempt
def email(request):
    if request.method == "POST":
        data = json.loads(request.body)

        email = data["email"]
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return DefaultResponse(200, '사용 가능한 이메일입니다.')

        return DefaultResponse(400, '중복된 이메일입니다.')
