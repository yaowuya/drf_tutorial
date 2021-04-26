# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Author :        zhongrf
   Date：          2021/3/10
-------------------------------------------------
"""
from rest_framework import serializers
from .models import Course
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        filed = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段，只读

    class Meta:
        model = Course
        # exclude=('id',) #注意元组中只有一个元素时不能写成("id")
        # fields  = ( 'name', 'introduction', 'teacher', 'price')
        fields = '__all__'
        depth = 2

# class CourseSerializer(serializers.HyperlinkedModelSerializer):
#     teacher = serializers.ReadOnlyField(source='teacher.username')  # 外键字段，只读
#
#     class Meta:
#         model = Course
#         fields = ('id', 'name', 'introduction', 'teacher', 'price', 'created_at', 'update_at')
