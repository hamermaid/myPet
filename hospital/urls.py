# -*- coding: utf-8 -*-
from django.urls import path

from hospital.views import info

app_name = 'hospital'

urlpatterns = [
    path('info/<str:hos_id>', info, name='info'),
]
