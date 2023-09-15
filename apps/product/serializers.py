# -*- coding: utf-8 -*-
"""
@Project ：gykj_test 
@File    ：serializers.py
@IDE     ：PyCharm 
@Author  ：Lijintao
@Date    ：2023/9/15 23:13 
"""
from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'category')
