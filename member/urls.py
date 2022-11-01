# -*- coding: utf-8 -*-
from django.urls import path

from member.views import signup, login, email

app_name='member'

urlpatterns = [
    path('signup', signup, name='signup'), # 회원가입
    path('login', login, name='login'),    # 로그인
    path('email/duplicate', email, name='email'), # 이메일 중복확인
]
