# -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, customRes, defaultRes

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customRes/', customRes, name='customRes'),
    path('defaultRes/', defaultRes, name='defaultRes'),
]
