# -*- coding: utf-8 -*-
from django.urls import path

from member.views import signup, login

app_name='member'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
