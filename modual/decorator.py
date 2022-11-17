import datetime

import jwt
from django.contrib.auth.models import User

from member.models import Profile
from modual.response import DefaultResponse
from myPet.settings import SECRET_KEY


class TokenCheck:
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, request, *args, **kwargs):
        token = request.headers.get("Authorization", None)  # 헤더에서 access 토큰 가져옴
        try:
            if token:
                token_payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                user = User.objects.get(username=token_payload['id'])
                time = int(token_payload['exp']) - int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                # 토큰 유효시간 검사 - 유효시간 만료일 경우
                if time < 0:
                    refresh = request.headers.get("Refresh", None)  # 헤더에서 refresh 토큰 가져옴
                    # refresh 토큰 없음
                    if refresh is None:
                        return DefaultResponse(402, '만료된 토큰입니다.')
                    # refresh 토큰 인가 확인
                    profile = Profile.objects.get(user_id=user.username)
                    if profile.refresh_token != refresh:
                        return DefaultResponse(401, '잘못된 토큰입니다')
                    # refresh 토큰 유효시간 확인
                    refresh_payload = jwt.decode(refresh, SECRET_KEY, algorithms="HS256")
                    time = int(refresh_payload['exp']) - int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                    if time < 0:
                        return DefaultResponse(403, '재로그인이 필요합니다.')
                    access = {
                        'id': user.username,
                        'exp': (datetime.datetime.now() + datetime.timedelta(minutes=60)).strftime("%Y%m%d%H%M%S"),
                        'iat': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                        "token_type": "access",
                    }
                    acc_token = jwt.encode(access, SECRET_KEY, algorithm="HS256").decode('utf8')
                    return DefaultResponse(200, {"access": acc_token})      # 토큰 재발급
                request.user = user
                return self.original_function(self, request, *args, **kwargs)

            return DefaultResponse(401, '잘못된 토큰입니다.')

        except jwt.ExpiredSignatureError:
            return DefaultResponse(401, {'message':'EXPIRED_TOKEN'})

        except jwt.DecodeError:             # decode 실패
            return DefaultResponse(401, '잘못된 토큰입니다.')

        except User.DoesNotExist:           # access에서 추출한 id를 가진 회원이 없을떄
            return DefaultResponse(400, '잘못된 사용자입니다')


def token_required(function):
    def wrap(request, *args, **kwargs):
        token = request.headers.get("Authorization", None)  # 헤더에서 access 토큰 가져옴
        try:
            if token:
                token_payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
                user = User.objects.get(username=token_payload['id'])
                time = int(token_payload['exp']) - int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                # 토큰 유효시간 검사 - 유효시간 만료일 경우
                if time < 0:
                    refresh = request.headers.get("Refresh", None)  # 헤더에서 refresh 토큰 가져옴
                    # refresh 토큰 없음
                    if refresh is None:
                        return DefaultResponse(402, '만료된 토큰입니다.')
                    # refresh 토큰 인가 확인
                    profile = Profile.objects.get(user_id=user.username)
                    if profile.refresh_token != refresh:
                        return DefaultResponse(401, '잘못된 토큰입니다')
                    # refresh 토큰 유효시간 확인
                    refresh_payload = jwt.decode(refresh, SECRET_KEY, algorithms="HS256")
                    time = int(refresh_payload['exp']) - int(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
                    if time < 0:
                        return DefaultResponse(403, '재로그인이 필요합니다.')
                    access = {
                        'id': user.username,
                        'exp': (datetime.datetime.now() + datetime.timedelta(minutes=60)).strftime("%Y%m%d%H%M%S"),
                        'iat': datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
                        "token_type": "access",
                    }
                    acc_token = jwt.encode(access, SECRET_KEY, algorithm="HS256").decode('utf8')
                    return DefaultResponse(200, {"access": acc_token})  # 토큰 재발급
                request.user = user
                return function(request, *args, **kwargs)

            return DefaultResponse(401, '잘못된 토큰입니다.')

        except jwt.ExpiredSignatureError:
            return DefaultResponse(401, {'message': 'EXPIRED_TOKEN'})

        except jwt.DecodeError:  # decode 실패
            return DefaultResponse(401, '잘못된 토큰입니다.')

        except User.DoesNotExist:  # access에서 추출한 id를 가진 회원이 없을떄
            return DefaultResponse(400, '잘못된 사용자입니다')
    return wrap