# -*- coding: utf-8 -*-
from django.urls import path

from hospital.views import list

app_name = 'hospital'

urlpatterns = [
    path('list/', list, name='list'),
]
