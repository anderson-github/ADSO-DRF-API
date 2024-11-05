from rest_framework import serializers
from .models import Products, UsersProducts


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = [
            'id',
            'product_name',
            'product_price',
            'product_type',
            'product_stock'
        ]


class UsersProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersProducts
        fields = [
            'id',
            'selling_date',
            'products_amount',
            'client',
            'product',
        ]


class UsersProductsOutputSerializer(serializers.Serializer):
    pass
