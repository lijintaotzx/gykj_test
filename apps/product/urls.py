# -*- coding: utf-8 -*-
"""
@Project ：gykj_test 
@File    ：urls.py
@IDE     ：PyCharm 
@Author  ：Lijintao
@Date    ：2023/9/15 23:04 
"""
from django.urls import path

from .views import ProductListView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
]
