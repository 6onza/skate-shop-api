from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'name', 'description', 'price', 'image_1','image_2', 'image_3', 'size', 'category', 'created_at', 'updated_at']

    def get_size(self, product):
        return product.size.values_list('name', flat=True)
