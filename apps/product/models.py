# -*- coding: utf-8 -*-
"""
@Project ：gykj_test
@File    ：urls.py
@IDE     ：PyCharm
@Author  ：Lijintao
@Date    ：2023/9/15 23:04
"""
from django.db import models


class Category(models.Model):
    """ 分类表"""
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ 产品表"""
    name = models.CharField(max_length=128, )
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.SET_NULL)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name
