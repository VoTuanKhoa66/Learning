from .import models
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = '__all__'

class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductComment
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    product_comment = ProductCommentSerializer(many=True, read_only=True)
    class Meta:
        model = models.Product
        fields = (
            'id',
            'name',
            'unit',
            'price',
            'discount',
            'amount',
            'is_public',
            'thumbnail',
            'product_image',
            'product_comment',
            'category_id',
            'created_at',
            'updated_at',
            'deleted_at'
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'slug',
            'icon_url',
            'products',
            'created_at',
            'updated_at',
            'deleted_at'
        )

