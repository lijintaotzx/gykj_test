# -*- coding: utf-8 -*-
from django.db import connection
from rest_framework import generics

from .serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        with connection.cursor() as cursor:
            # Execute raw SQL query to fetch product and category data
            cursor.execute('''
                SELECT
                    p.id,
                    p.name,
                    c.id AS category_id,
                    c.name AS category_name
                FROM
                    product_product p
                LEFT JOIN
                    product_category c
                ON
                    p.category_id = c.id
            ''')
            # Fetch the results and return them as a queryset
            results = cursor.fetchall()
            queryset = [
                {
                    'id': row[0],
                    'name': row[1],
                    'category': {
                        'id': row[2],
                        'name': row[3]
                    }
                } for row in results
            ]
            return queryset
