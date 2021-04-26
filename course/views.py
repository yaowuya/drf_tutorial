# -*- coding: utf-8 -*-
# Create your views here.
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# course_dict = {
#     'name': '课程名称',
#     'introduction': '课程介绍',
#     'price': 0.11,
# }
#
#
# # 使用Django FBV 编写API接口
# @csrf_exempt
# def course_list(request):
#     if request.method == 'GET':
#         # return HttpResponse(json.dumps(course_dict), content_type='application/json')
#         return JsonResponse(course_dict)
#     if request.method == 'POST':
#         course = json.loads(request.body.decode('utf-8'))
#         return JsonResponse(course, safe=False)
#
#
# # Django CBV 编写API接口
# @method_decorator(csrf_exempt, name='dispatch')
# class CourseList(View):
#     def get(self, request):
#         return JsonResponse(course_dict)
#
#     def post(self, request):
#         course = json.loads(request.body.decode('utf-8'))
#         return JsonResponse(course, safe=False)
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

from course.models import Course
from course.serializers import CourseSerializer

"""一、函数式编程 Function Based View"""


@api_view(["GET", "POST"])
def course_list(request):
    """
    获取所有课程信息或新增一个课程
    :param request:
    :return:
    """
    if request.method == "GET":
        course = CourseSerializer(instance=Course.objects.all(), many=True)
        return Response(data=course.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        course = CourseSerializer(data=request.data)  # 部分更新 partial=True
        if course.is_valid():
            course.save(teacher=request.user)
            return Response(data=course.data, status=status.HTTP_201_CREATED)
        return Response(course.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def course_detail(request, pk):
    """
    获取、更新、删除一个课时
    :param request:
    :return:
    """
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        s = CourseSerializer(instance=course)
        return Response(data=s.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        s = CourseSerializer(instance=course, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_200_OK)
    if request.method == "DELETE":
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""二、类视图 Class Based View"""


class CourseList(APIView):
    def get(self, request):
        """
        :param request:
        :return:
        """
        queryset = Course.objects.all()
        s = CourseSerializer(instance=queryset, many=True)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        :param request:
        :return:
        """
        s = CourseSerializer(data=request.data)
        if s.is_valid():
            s.save(teacher=self.request.user)
            print(type(request.data), type(s.data))
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return

    def get(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        s = CourseSerializer(instance=obj)
        return Response(data=s.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        s = CourseSerializer(instance=obj, data=request.data)
        if s.is_valid():
            s.save()
            return Response(data=s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        if not obj:
            return Response(data={"msg": "没有此课程信息"}, status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""三、通用类视图 Generic Class Based View"""


class GCourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class GCourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


"""四、DRF的视图集viewsets"""


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)
