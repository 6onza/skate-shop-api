from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_size(self, product):
        return product.size.values_list('name', flat=True)
