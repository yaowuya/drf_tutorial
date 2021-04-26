# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Author :        zhongrf
   Date：          2021/3/10
-------------------------------------------------
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from course import views

router = DefaultRouter()
router.register(prefix="viewsets", viewset=views.CourseViewSet)

urlpatterns = [
    # Function Based View
    path("fbv/list/", views.course_list, name="fbv-list"),
    path("fbv/detail/<int:pk>/", views.course_detail, name="fbv-detail"),
    # Class Base View
    path("cbv/list/", views.CourseList.as_view(), name="cbv-list"),
    path("cbv/detail/<int:pk>/", views.CourseDetail.as_view(), name="cbv-detail"),
    # Generic Class Based View
    path("gcbv/list/", views.GCourseList.as_view(), name="gcbv-detail"),
    path("gcbv/detail/<int:pk>/", views.GCourseDetail.as_view(), name="gcbv-detail"),
    # DRF viewsets
    path("", include(router.urls))
]
